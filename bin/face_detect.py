#import sys
import cv2

#import sys
#sys.path.insert(0,'..')
import os
from config import *

# This shiz works like charm 

def face_detect(photo_name):
    # Load the cascade
    cwd = os.getcwd()
    #print(cwd)
    
    him = (cwd + '\\bin\\lib\\haarcascade_frontalface_default.xml')
    #print(him)
    
    print(him)

    face_cascade = cv2.CascadeClassifier(him)
        
    pim = (cwd + '\\resource\\passport_size_photo\\' + photo_name)
    print(pim)

    # Read the input image
    img = cv2.imread(pim)
    #img = cv2.imread('nig.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if any(map(lambda x: any(x), faces)):
        print("Face detected in image !")   
        if show_output_boxes == True:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('Face', img)
            #cv2.waitKey()
        return True
    
    else:
        print("No Face Detected !")
        return False
