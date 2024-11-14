# Asana-Check_Yoga-Pose-Validating-Web-Application
This repository contains a machine-learning model that evaluates yoga poses based on images uploaded by users. The model is built using the VGG19 architecture and is designed to provide feedback on the correctness of the pose. The web application is developed using Flask, allowing users to interact with the model seamlessly.

## Overview
This project aims to provide real-time feedback on yoga pose accuracy. By analyzing a user-uploaded image, the model determines if the pose aligns with the expected posture. This tool is useful for yoga practitioners looking for immediate guidance on their form.

## Model Architecture
- **VGG19**: A deep convolutional neural network known for its effectiveness in image classification tasks.
- **TensorFlow**: A powerful open-source machine learning framework for building and training the model.

## Dependencies
- TensorFlow
- Pillow
- Matplotlib
- NumPy
- Pandas
- Flask

## Setup and Installation
### Prerequisites
- Python 3.7+
- TensorFlow, Flask, and other libraries in requirements.txt

### Installation
1. Clone this repository:
   ```git clone https://github.com/yourusername/Asana-Check_Yoga-Pose-Validating-Web-Application.git```
    ```cd Asana-Check_Yoga-Pose-Validating-Web-Application```
   
3. Install the required libraries:
`pip install -r requirements.txt`

5. Run the Flask application:
   `python app.py`
   
7. Access the web app at `http://127.0.0.1:5000`.

## Usage
1. Open the web app in your browser.
2. Upload an image of your yoga pose.
3. Submit the image to get validation.

## Credits
- Yoga Poses Dataset: [Kaggle](https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset)

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
