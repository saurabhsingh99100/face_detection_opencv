import cv2
capture = cv2.VideoCapture(0) 
face_classifier = cv2.CascadeClassifier('face.xml')  
 
while capture:   
    ret, img = capture.read()
    img = cv2.flip(img, +1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_classifier.detectMultiScale(gray, 1.3, 5) 
  
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        coordinates=(x+w/2,y+w/2)
        print(coordinates)
    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release() 
 
cv2.destroyAllWindows()