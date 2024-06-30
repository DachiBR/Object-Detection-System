import cv2

class Camera:
    def __init__(self, camera_index=1):  # Default to the first USB camera
        self.video_capture = cv2.VideoCapture(camera_index)

    def get_frame(self):
        ret, frame = self.video_capture.read()
        return ret, frame

    def release(self):
        self.video_capture.release()
