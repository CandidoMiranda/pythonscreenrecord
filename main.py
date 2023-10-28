import cv2
import keyboard
import pyautogui
import numpy as np

# Set fps
fps = 30

# Get the resolution with pyautogui.size() but it is a object and cast it to a tuple
screenResolution = tuple(pyautogui.size())

# avi codec -> XVID
codec = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter("video.avi", codec, fps, screenResolution)

while True:
    # get a screenshot
    frame = pyautogui.screenshot()
    # transform the screenshot in a numpy array
    frame = np.array(frame)
    # cv2 use GBR color, this line convert the RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # write the screenshot (frame) in the video
    video.write(frame)

    # stop screen record
    if keyboard.is_pressed('esc'):
        break

# release the video
video.release()
# it's not necessary buy is a good practice
cv2.destroyAllWindows()