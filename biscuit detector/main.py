import cv2
import numpy as np
import os
import time


camera_index = 0
resolution = (1280, 720)
fps = 30

cap = cv2.VideoCapture(camera_index)


def make_720p():
    global resolution
    resolution = (1280, 720)
    #cap.set(10, 160)
    cap.set(3, resolution[0])
    cap.set(4, resolution[1])


def process_frame(frame):
    global x, y, w, h
    global fps

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([10, 50, 50])
    upper_bound = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        
def print_info():
    global fps
    print("Camera Index:", camera_index)
    print("Resolution:", resolution)
    print("FPS:", fps)

def quit_application():
    cap.release()
    cv2.destroyAllWindows()


start_time = time.time()
print_info()
make_720p()
cv2.namedWindow("Webcam")

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    
    if not ret or frame is None:
        print("Error: Failed to capture frame.")
        break

        process_frame(frame)
    
    cv2.imshow("Webcam", frame)

    elapsed_time = time.time() - start_time
    fps = 1 / elapsed_time
    start_time = time.time()
