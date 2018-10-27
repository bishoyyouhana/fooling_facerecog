# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:26:46 2018

@author: Bishoy
"""

from PIL import Image, ImageDraw
import face_recognition
import os

i=0
os.chdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\results")
image_names=os.listdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\results')
for imagelolz in image_names:
    image = face_recognition.load_image_file(imagelolz)

# Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

    for face_landmark in face_landmarks_list:

        # Print the location of each facial feature in this image
        for facial_feature in face_landmark.keys():
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmark[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)
        
        for facial_feature in face_landmark.keys():
            d.line(face_landmark[facial_feature], width=5)

        #pil_image.show()
        pil_image.save("face_landmarks {}.jpg".format(i))
        i+=1

input("press enter to exit")
    