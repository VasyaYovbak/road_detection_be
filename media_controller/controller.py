from flask import request, send_file, Blueprint

from PIL import Image
from ultralytics import YOLO

from detection import detect_image, detect_video
import torch_directml

dml = torch_directml.device()

media_controller_blueprint = Blueprint('media_controller_blueprint', __name__)

model_pothole = YOLO("static/best_pothole.pt")
model_traffic = YOLO("static/best_tl.pt")
model_pothole.to(dml)
model_traffic.to(dml)



@media_controller_blueprint.route('/api/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image file provided', 400
    image = Image.open(request.files['image'])
    result_image = detect_image(model_pothole, model_traffic, image)
    Image.fromarray(result_image).save('results/result_image.png')
    response = send_file('results/result_image.png')
    return response


@media_controller_blueprint.route('/api/upload-video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video file provided', 400
    temp_file = "temp_video.mp4"
    request.files['video'].save(temp_file)
    detect_video(model_pothole, model_traffic, temp_file)
    return send_file("result_video.webm"), 200
