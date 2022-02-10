import cv2

from config import *

import bin.face_detect as fd
import bin.signature_detection as sd


# Will add logic to get passport size photo from database using user id & signature of the user via same method, rn left it blank
n1 = 'test'
n2 = 'sig'

result_1 = fd.face_detect(n2)
result_2 = sd.signature_detect(n1)

cv2.waitKey()