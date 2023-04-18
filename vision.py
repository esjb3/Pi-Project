import cv2 as cv
import argparse

from ultralytics import YOLO
import supervision as sv

class Vision:
    def __init__(self, model, source):
        self.model = YOLO(model + ".pt")
        self.cap = cv.VideoCapture(source)

        # THE FOLLOWING SHOULD BE SET TO THE RESOLUTION OF OUR CAMERA
        # self.cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
        # self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)

    def detect(self):
        _, frame = self.cap.read()

        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        detected = {
            "person": False,
            "vehicle": False,
            "obstruction": False,
        }

        for d in detections:
            conf, class_id = d[2], d[3]

            if conf < 0.65:
                continue

            if class_id == 0:
                detected["person"] = True
            elif class_id in [2, 3]:
                detected["vehicle"] = True
            else:
                detected["obstruction"] = True

        return detected
