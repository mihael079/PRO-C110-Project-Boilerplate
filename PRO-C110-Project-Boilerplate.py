# for capturing frames from webcam
import cv2

# for processing images
import numpy as np

# attaching webcam indexed as 0 with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

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

        # if 'space' key is pressed, break
        if code  ==  32:
            break

camera.release()
cv2.destroyAllWindows()
