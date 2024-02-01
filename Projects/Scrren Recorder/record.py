import cv2
import numpy as np
import pyautogui
import time
from win32api import GetSystemMetrics

# video screen size 
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("record1.mp4", f, 30.0, dim)

# Video duration 
start_time = time.time()
dur = 14
end_time = start_time + dur

# Forming video by joining images 
while True:
    images = pyautogui.screenshot()
    frames = np.array(images)
    frame = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)  #For original color
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()