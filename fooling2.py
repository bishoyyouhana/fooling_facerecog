import face_recognition
from PIL import Image
import os
import timeit

start = timeit.default_timer()
i=0
filenames=os.listdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics")
os.chdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics")
for the_image in filenames:
    image=face_recognition.load_image_file(the_image)

    face_locations=face_recognition.face_locations(image)
    print("i found {} faces in this photograph".format(len(face_locations)))
    
    
    for face_location in face_locations:
        top, right,bottom,left = face_location
        print("a face location at pixel top:{}, left:{}, bottom:{}, right:{}".format(top,left,bottom,right))
        face_image= image[top:bottom, left:right]
        pil_image=Image.fromarray(face_image)
        os.chdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\results")
        pil_image.save("face -{}.jpg".format(i))
        os.chdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\test_pics")
        i+=1
    #os.remove(the_image)
stop = timeit.default_timer()
print(stop -start)

#pil_image.save("../results/")

