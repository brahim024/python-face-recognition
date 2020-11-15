import cv2
import numpy as np
img=cv2.imread('resource/elon-musk.jpg')
print(img.shape)
imgresise=cv2.resize(img,(450,450))
cv2.imshow('resise',imgresise)
cv2.waitKey(0)