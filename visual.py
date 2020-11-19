import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread('resource/linus.jpg')
imgcanny=cv2.Canny(img,5,100)
imgeroded=cv2.erode(imgcanny,kernel,iterations=2)
imgDialtion=cv2.dilate(img,kernel,iterations=2)
cv2.imshow('dialation',imgDialtion)
cv2.imshow('erod',imgeroded)

cv2.waitKey(0)