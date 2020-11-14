import cv2
cap=cv2.VideoCapture('resource/video-test.mp4')
while True:
	secess,img=cap.read()
	cv2.imshow('video',img)
	if cv2.waitKey(1)& 0xFF ==ord('b'):
		break