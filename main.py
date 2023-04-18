from vision import Vision

class Main(Vision):
    def __init__(self):
        super().__init__("yolov8n", 0)

    def process_frame(self):
        d = super().detect()
        
        if d["car"]:
            # DO NOT GO ALERT TO WALKER
            pass
        elif d["obstruction"]:
            # POSSIBLE OBSTRUCTION ALERT TO WALKER
            pass
        if d["person"]:
            # FLASHING LIGHT TO INDICATE POSSIBLE
            # PEDESTRIAN ON CROSSWALK TO ONCOMNIG TRAFFIC
            pass

    def start(self):
        while True:
            self.process_frame()

main = Main()
main.start()
