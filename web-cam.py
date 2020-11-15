import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,720)
cap.set(10,100)
while True:
	secess,img=cap.read()
	imgcanny=cv2.Canny(img,50,100)
	imgBlur=cv2.GaussianBlur(img,(3,3),0)
	cv2.imshow('video',img)
	cv2.imshow('canny',imgcanny)
	cv2.imshow('blur',imgBlur)

	if cv2.waitKey(1)& 0xFF ==ord('b'):
		break
