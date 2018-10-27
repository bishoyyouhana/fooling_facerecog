# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:59:01 2018

@author: Bishoy
"""
from PIL import Image
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
    
crop(r"C:\Users\Win8.1\source\repos\fooling_facerecog\tendicles.jpg",(161, 166, 706, 1050),r"C:\Users\Win8.1\source\repos\fooling_facerecog\tendicles.jpg")