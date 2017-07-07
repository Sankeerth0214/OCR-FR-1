import cv2
import numpy as np
list=[]
vidcap = cv2.VideoCapture('b.mp4')
success,image = vidcap.read()
count = 0
print "I am in success"
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(01) == 10:                     # exit if Escape is hit
      break
  list.append("frame%d.jpg" % count)
  count += 1
print(list)
for name in list:
	face_cascade = cv2.CascadeClassifier('/home/sowjanya/Desktop/frontalFace10/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('/home/sowjanya/Desktop/frontalFace10/haarcascade_frontalface_default.xml')
	img = cv2.imread(name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.02, 5)
	for (x,y,w,h) in faces:
    		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    		roi_gray = gray[y:y+h, x:x+w]
    		roi_color = img[y:y+h, x:x+w]
    		eyes = eye_cascade.detectMultiScale(roi_gray)
    		for (ex,ey,ew,eh) in eyes:
        		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			cv2.imshow('img',img)
			#cv2.imwrite("a%d.jpg" % count, image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
