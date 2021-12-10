# for captureing frames from webcam
import cv2

# for processing images
import numpy as np

# attaching webcam indexed as 0 with the application software
camera = cv2.VideoCapture(0)

# while camera is connected with the applcation software
while camera.isOpened():

    # requesting a frame from camera
    status , frame = camera.read()

    # if we were able to capture the frame successfully, status is 'true'
    if status:

        # flipping the frame
        frame = cv2.flip(frame , 1)

        # displaying the video feed
        cv2.imshow('video feed' , frame)

        # waiting for key press for 1ms
        code = cv2.waitKey(1)

        # if 'b' key is pressed, break
        if code  ==  ord('b'):
            break

camera.release()
cv2.destroyAllWindows()