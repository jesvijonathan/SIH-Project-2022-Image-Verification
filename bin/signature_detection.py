import cv2
import os
from config import *

def signature_detect(sign_name):
    cwd = os.getcwd()
    #print(cwd)

    image = cv2.imread(cwd + "\\resource\\signature_photo\\" + sign_name + ".jpg", 1)

    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,img)
    cv2.bitwise_not(img,img)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))

    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, rect_kernel)
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #contours, hier = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # set show_output_boxes in config to true to see what it has considered as a signature
        print("Possible signature detected !")
        if show_output_boxes == True:
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                if(h>20):
                    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)
            cv2.imshow("Result", image)
        cv2.waitKey()
        return True
        
    else:
        print("No signtaure found !")
        return False