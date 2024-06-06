# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
import tensorflow as tf

model = tf.keras.models.load_model("converted_keras/keras_model.h5")


# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		
		ret, frame = vid.read()
		img =cv2.resize(frame,(224,224))
		testimg = np.array(img,dtype=np.float32)
		print(testimg)
		testimg=np.expand_dims(testimg,axis=0)
		print(testimg)
		normalisedimages =testimg/255.0
		prediction=model.predict(normalisedimages)
		print("Prediction: ",prediction)
		  
		    # Display the resulting frame
		cv2.imshow('frame', frame)
		      
		    # Quit window with spacebar
		key = cv2.waitKey(1)
		    
		if key == 32:
		    break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
