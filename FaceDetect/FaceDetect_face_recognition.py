
import cv2
import sys

import face_recognition

# Get user supplied values
# imagePath = sys.argv[1]
imagePath = "/Users/rex/Desktop/Code/Intelligence_classroom/image/1normal4.jpg"

# Load the image from face_recognition
image = face_recognition.load_image_file(imagePath)

# Detect faces in image

face_loaction = face_recognition.face_locations(image)

print("Found {0} Faces!".format(len(face_loaction)))

# Read the image with openCV

image = cv2.imread(imagePath)

# Draw a rectangle around the faces
for(top, right, bottom, left) in face_loaction:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

cv2.imshow("Faces found", cv2.resize(image,(1024,768)))
cv2.waitKey(0)