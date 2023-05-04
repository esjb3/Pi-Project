import cv2 as cv
import time

from collections import deque
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

CLEAR = 0
CAUTION = 1
DANGER = 2

class Vision:
    def __init__(self, model, source="0"):
        self.model = YOLO(model + ".pt")
        self.source = source
        self.cache = deque([], 5)

    def status(self):
        status = CLEAR
        for s in self.cache:
            if s == DANGER:
                status = DANGER
            if s == CAUTION:
                status = CAUTION
        return status

    def detect(self):
        results = self.model(self.source, True, verbose=False)

        for r in results:
            annotator = Annotator(r.orig_img)

            status = CLEAR
            self.person = False
            self.pcount = 0
            self.ccount = 0
            for box in r.boxes:
                coords, cid, conf = box.xyxy[0], int(box.cls), float(box.conf)

                if conf < 0.65:
                    continue

                annotator.box_label(coords, self.model.names[cid])

                if cid == 0:
                    self.person = True
                    self.pcount += 1
                elif cid in [2, 3, 67]:
                    status = DANGER
                    self.ccount += 1
                elif status != DANGER:
                    status = CAUTION
            self.cache.append(status)

            frame = annotator.result()
            yield frame
