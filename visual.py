import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread('resource/linus.jpg')
imgcanny=cv2.Canny(img,5,100)

imgDiaaltion=cv2.dilate(imgcanny,kernel,iterations=5)
cv2.imshow('dialation',imgDiaaltion)
cv2.waitKey(0)