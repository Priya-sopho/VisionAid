#pip --no-cache-dir install face_recognition
#pip install cv2

import time
import cv2
import face_recognition

"""
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(5)  # If you don't wait, the image will be dark
return_value, image = camera.read()
time.sleep(2)
raw_input() #To take next image
return_value, unknown_image = camera.read()

cv2.imshow("img1", image)
cv2.imshow("img2",unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

biden_encoding = face_recognition.face_encodings(image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)
del(camera)  # so that others can use the camera as soon as possible
"""

class SecurityCamera:
	camera_port = 0
	
	def __init__(self):
		self.camera = cv2.VideoCapture(self.camera_port)
		time.sleep(5) #To capture a clear image
		self.initial_encoding = self.FaceEncoding()

	
    #To return the face_encoding of captured image. It will retake images untill face is not found
	def FaceEncoding(self):
		while True:
			return_value, image = self.camera.read()
			if len(face_recognition.face_encodings(image))>0:
				return face_recognition.face_encodings(image)[0]

	
	#To compare two images taken at two different period of time
	def compare(self):
		unknown_encoding = self.FaceEncoding()
		results = face_recognition.compare_faces([self.initial_encoding],unknown_encoding)
		return results

    
    #destructor function
	def __del__(self):
		del(self.camera) #so that others can use the camera as soon as possible



security = SecurityCamera()
time.sleep(5)
if (security.compare()):
	print "Wooh!!! You are the same person"
else:
	print "Failed to recognize you!!"
