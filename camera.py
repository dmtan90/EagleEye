
import cv2 
import matplotlib.pyplot as plt

cameraMap = dict()

class Camera:
    def __init__(self, camType="webcam", resolution = (640, 480)):
        self.camera = cameraMap[camType](resolution)
    
    def getFrame(self):
        return self.camera.getFrame()

class webCam(Camera):
    def __init__(self, resolution = (640, 480)):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    def getFrame(self):
        ret, frame = self.camera.read()
        frame = cv2.flip(frame,1)
        return frame

class piCam(Camera):
    def __init__(self, resolution = (640, 480)):
        from picamera.array import PiRGBArray
        from picamera import PiCamera
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=(640, 480))
    def getFrame(self):
        frame = camera.capture(rawCapture, format="bgr", use_video_port=True)
        rawCapture.truncate(0)
        return frame

cameraMap['rpi'] = piCam
cameraMap['webcam'] = webCam