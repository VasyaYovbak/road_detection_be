import cv2


def get_prediction(model_pothole, model_traffic, image):
    results = model_pothole(image)  # predict on an image
    probability_threshold = 0.5
    boxes = []
    for i in range(len(results[0].boxes.conf)):
        if results[0].boxes.conf[i] >= probability_threshold:
            boxes.append(results[0].boxes[i])
    results[0].boxes = boxes
    res_plotted = results[0].plot()

    results = model_traffic(res_plotted)
    boxes = []
    for i in range(len(results[0].boxes.conf)):
        if results[0].boxes.conf[i] >= probability_threshold:
            boxes.append(results[0].boxes[i])
    results[0].boxes = boxes

    return results


def detect_image(model_pothole, model_traffic, image):
    return get_prediction(model_pothole, model_traffic, image)[0].plot()[:, :, ::-1]


def detect_video(model_pothole, model_traffic, video):
    cap = cv2.VideoCapture(video)

    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_count = 0

    output = cv2.VideoWriter('result_video.webm', cv2.VideoWriter_fourcc(*'VP80'), fps / 2, (w, h))

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            if frame_count % 2 == 0:
                pred = get_prediction(model_pothole, model_traffic, frame)

                output.write(pred[0].plot())
            frame_count += 1
        else:
            break

    cap.release()
    output.release()
