import os

from flask import Flask, request, send_file
from flask_cors import CORS

from ultralytics import YOLO

from PIL import Image

from yovo_detection import detect_image, detect_video

app = Flask(__name__)

CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image file provided', 400

    image = Image.open(request.files['image'])
    result_image = detect_image(model_pothole, model_traffic, image)
    Image.fromarray(result_image.astype('uint8')).save('results/result_image.png')

    return send_file('results/result_image.png'), 200


@app.route('/api/upload-video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video file provided', 400
    temp_file = "temp_video.mp4"
    request.files['video'].save(temp_file)
    detect_video(model_pothole, model_traffic, temp_file)
    os.remove(temp_file)
    return send_file("result_video.webm"), 200


if __name__ == '__main__':
    global model_pothole, model_traffic
    model_pothole = YOLO("best.pt")
    model_traffic = YOLO("best_traffic_2.pt")
    app.run(debug=1)
