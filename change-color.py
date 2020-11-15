import cv2
img=cv2.imread('resource/lesly_zerna.png')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY )
imgBlur=cv2.GaussianBlur(imgGray,(3,3),0)
imgcanny=cv2.Canny(img,5,100)
cv2.imshow('gray',imgGray)
cv2.imshow('blur',imgBlur)
cv2.imshow('canny',imgcanny)
cv2.waitKey(0)