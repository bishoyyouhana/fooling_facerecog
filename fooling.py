# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:13:29 2018

@author: Bishoy
"""
import face_recognition
from PIL import Image
import os
import timeit
from numba import vectorize
from inspect import signature

#@vectorize(['float32(float32, float32)'], target='cuda')
'''
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
    '''
def amir(path_of_images, results):
    start = timeit.default_timer()
    os.chdir(path_of_images)
    picslist=os.listdir(path_of_images)
    n=1
    i=0
    for pic in picslist:
        image = face_recognition.load_image_file(pic)
        face_locations = face_recognition.face_locations(image)
        print(face_locations)
        for face_location in face_locations:
            intimer=timeit.default_timer()
            os.chdir(results)
            i=1
            top=face_location[0]
            left=face_location[3]
            bottom=face_location[2]
            right=face_location[1]
            print("A face located at pixel Top: {}, left: {}, bottom: {}, right: {}".format(top,left,bottom,right))
            face_image = image[top:bottom,left:right]
            pil_image=Image.fromarray(face_image)
            pil_image.save("face--{}-{}.jpg".format(i,n))
            os.chdir(results)
            i +=1
            stoptimer=timeit.default_timer()
        n +=1
        #os.remove(pic)
        stop = timeit.default_timer()
        print("from beginning: ",stop -start)
        print("for pic: ",stoptimer-intimer)
    input("press enter to exit")
amir("C:\\Users\\Win8.1\\source\\repos\\fooling_facerecog\\test_pics","C:\\Users\\Win8.1\\source\\repos\\fooling_facerecog\\results")
    #crop(r"C:\Users\Win8.1\source\repos\fooling_facerecog\biden.jpg",(left,top,right,bottom),r"C:\Users\Win8.1\source\repos\fooling_facerecog\biden.jpg")
    #face_locations(img, number_of_times_to_upsample=1, model='hog')
    
#65,215,169,112