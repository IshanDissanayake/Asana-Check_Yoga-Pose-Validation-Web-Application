import os
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.preprocessing import image

#app intializing
app = Flask(__name__)
app.secret_key = 'supersecuritykey'

#loading model
model = load_model('YogaPoseModel.h5')

#defining pose names 
poses = ['Downdog', 'Goddess', 'Plank', 'Tree', 'Worrior2']

#creating a folder to save the uploaded image
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        #getting pose and file
        pose = request.form.get('pose')
        file = request.files.get('file')

        if pose not in poses:
            flash('Please select a valid Yoga Pose', 'error')
            return redirect(url_for('index'))

        if file and file.filename == '':
            flash('Please upload an image', 'error')
            return redirect(url_for('index'))

        else:
            #saving the file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            #loading and preprocessing the image
            img = image.load_img(file_path, target_size=(224,224))
            img_arr = image.img_to_array(img)
            img_arr = np.expand_dims(img_arr, axis=0)
            img_data = preprocess_input(img_arr)

            #predicting the pose
            prediction = model.predict(img_data)
            predicted_class_index = np.argmax(prediction[0])
            predicted_pose = poses[predicted_class_index]

            #validation
            is_correct = (predicted_pose == pose)
            result_text = 'Correct Pose' if is_correct else 'Incorrect Pose'
            result_color = 'green' if is_correct else 'red'

            return render_template('index.html', poses=poses, result_text=result_text, result_color=result_color, file_path=file_path, selected_pose=pose)

    return render_template('index.html', poses=poses)

if __name__ == '__main__':
    app.run(debug=True)
