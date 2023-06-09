# Automatic Detection and Recognition of Traffic Lights and Potholes using YOLOv8 
# 1. Project Overview
This project uses the You Only Look Once (YOLO) algorithm, specifically its eighth version (YOLOv8), to automatically detect and recognize traffic lights and potholes.
# 2. Getting Started
All commands and scripts below are for Windows.
### Clone Git repository:
This command is used to obtain a repository from an existing URL.
>     git clone https://github.com/VasyaYovbak/road_detection_be.git
### Install packages with pip: -r requirements.txt
Use the command below to install the packages according to the configuration file **requirements.txt**.
>     pip install -r requirements.txt
# 3. Run the project
In order to launch the projects, you need to execute this command in the terminal:
 >    py app.py 
# 4. Additionally
# Training
1. Training the model to detect potholes:
In order to train the appropriate model, you should go to the notebook **"pothole_train.ipynb"** in folder **"train_models"**.  In this notebook , you should run the code step by line. 
The results of model training can be found in:
 >    runs/detect/train
2. Training the model to detect potholes:
In order to train the appropriate model, you should go to the notebook **"traffic_light_train.ipynb"** in folder **"train_models"**.  In this notebook , you should run the code step by line. 
The results of model training can be found in:
>  runs/detect/train
# Swagger
You can view endpoints using URL: 
> https://app.swaggerhub.com/apis/Julia47/trafficpotholes/1.0.0
