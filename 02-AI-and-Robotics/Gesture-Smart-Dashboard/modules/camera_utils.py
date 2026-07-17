import cv2
import time

# read 10 frames before open 
def open_laptop_camera(index=0, warmup_frames=10):
   
   #open camera  , cv2.CAP_AVFOUNDATION for macOS
    cap = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)

    if not cap.isOpened():
        return None
# Because camera is not stable in the first moments 
#  we wait amount of time
    for _ in range(warmup_frames):
        cap.read()
        time.sleep(0.05)

    return cap