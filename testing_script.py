# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:54:58 2018

@author: Bishoy
"""
from icrawler.builtin import GoogleImageCrawler

#from numba import vectorize
lads=input("who do you want to test on?")

no=int(input("how many pics?"))
def amin():
    google_crawler = GoogleImageCrawler(storage={'root_dir':r'C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics'})
    google_crawler.crawl(keyword=lads, max_num=no)
    done="done"
    print(done)
    return None

#@vectorize(['float32(float32, float32)'], target='cuda')

amin()
print("press enter to exit")


