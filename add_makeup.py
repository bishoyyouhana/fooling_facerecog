from PIL import Image, ImageDraw
import face_recognition
import os
# Load the jpg file into a numpy array
i=0
'''
makeupconf=True
makeupconf=input("do you want me to add default make up?")
if makeupconf==True:

    else:

'''
os.chdir(r"C:\Users\Win8.1\source\repos\fooling_facerecog\results")
image_names=os.listdir(r'C:\Users\Win8.1\source\repos\fooling_facerecog\results')
for imagelolz in image_names:
    image = face_recognition.load_image_file(imagelolz)

# Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    
    for face_landmarks in face_landmarks_list:
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image, 'RGBA')
        
        # Make the eyebrows into a nightmare
        d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=1)
        d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=1)
        
        # Gloss the lips
        d.polygon(face_landmarks['top_lip'], fill=(255, 0,0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(255, 0,0, 128))
        d.line(face_landmarks['top_lip'], fill=(255, 0,0, 64), width=1)
        d.line(face_landmarks['bottom_lip'], fill=(255, 0, 0, 64), width=1)
        
        # Sparkle the eyes
        d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

        # Apply some eyeliner
        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=2)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=2)
        
        #pil_image.show()
        pil_image.save("face_makeup {}.jpg".format(i))
        i+=1