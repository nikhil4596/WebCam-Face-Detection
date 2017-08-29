import cv2

image = cv2.imread('faces.jpg')
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(grayImg, 1.1, 5)
print (len(faces))
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y), (x+w, y+h), (255,255,0), 3)
cv2.imshow('face', image)
cv2.waitKey(0)
