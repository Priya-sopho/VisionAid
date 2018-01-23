#pip --no-cache-dir install face_recognition
#pip install cv2

import time
import cv2
import face_recognition
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(5)  # If you don't wait, the image will be dark
return_value, image = camera.read()
time.sleep(5)  # If you don't wait, the image will be dark
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