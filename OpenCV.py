import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
cap=cv2.VideoCapture(0) #cv2.data.haarcascades + 'cars.mp4'

while True:
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()
