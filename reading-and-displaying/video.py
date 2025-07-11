import cv2

cap = cv2.VideoCapture("videos/bibimbap.mp4")

while True:
    ret, frame = cap.read()

    cv2.imshow("Bibimbap", frame)

    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()