import time
import cv2
t_end= time.time() +10

cap = cv2.VideoCapture(0)


while time.time()< t_end:
	_, img=cap.read()
	# print time.time()
	cv2.putText(img, "Show Your face",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,25,255),2)
	
	cv2.imshow('Face match', img)
	# time.sleep(1)
	key = cv2.waitKey(10) & 0xFF

cv2.destroyAllWindows()

t_end= time.time() +10

while time.time()< t_end:
	_, img=cap.read()
	cv2.putText(img, "Show Your ID",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,25,255),2)

	# print time.time()
	cv2.imshow('img2', img)
	# time.sleep(1)
	key = cv2.waitKey(10) & 0xFF
