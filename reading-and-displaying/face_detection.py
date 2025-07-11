import cv2

face_cascade = cv2.CascadeClassifier('haar_frontalface.xml')
capture = cv2.VideoCapture('videos/bibimbap.mp4')

while True:
    ret, frame = capture.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rect = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, 
                                            minNeighbors=6)

    for (x,y,w,h) in faces_rect:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Face Detection on Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()