import time
import cv2
t_end= time.time() +10


face_cascade = cv2.CascadeClassifier('faceHaar.xml')

cap = cv2.VideoCapture(1)
print "Authentication System"

while time.time()< t_end:
	_, image=cap.read()
	# print time.time()
	cv2.putText(image, "Show Your face",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,25,255),2)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	face = face_cascade.detectMultiScale(gray, 1.3, 5)
	roi=gray.copy()
	for (x, y, w, h) in face:
		cv2.rectangle(image, (x, y), (x+w,y+h), (255, 0, 0), 2)
		roi= image[y:y+h, x:x+w]
	cv2.imshow("face", roi)
	cv2.imshow('Face match', image)
	# time.sleep(1)
	key = cv2.waitKey(10) & 0xFF
	if key == ord("q"):
		break
	cv2.imwrite("face.jpg", roi)	
cv2.destroyAllWindows()



t_end= time.time() +20
while time.time()< t_end:
	_, img=cap.read()
	cv2.putText(img, "Show Your ID",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,25,255),2)
	img = cv2.rectangle(img,(128,171),(460,330),(0,255,0),3)
	id= img[171:330, 128:460]
	gray = cv2.cvtColor(id, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	roi= gray.copy()
	face = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in face:
		cv2.rectangle(id, (x, y), (x+w,y+h), (255, 0, 0), 2)
		roi= img[y:y+h, x:x+w]
	cv2.imshow("roi", roi)
	# cv2.imshow("id", id)
	# print time.time()
	cv2.imshow('img2', img)
	# time.sleep(1)
	key = cv2.waitKey(10) & 0xFF
	if key == ord("q"):
		break	
	cv2.imwrite("face2.jpg", roi)
	