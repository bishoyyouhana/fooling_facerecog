# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:20:22 2018

@author: Bishoy
"""

import os

results=os.listdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\results')
test_pics = os.listdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics')
os.chdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\results')
for pic in results:
    os.remove(pic)
os.chdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics')
for pics in test_pics:
    os.remove(pics)
