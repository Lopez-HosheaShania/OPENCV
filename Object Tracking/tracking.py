import cv2

cap = cv2.VideoCapture('Videos/vid5.mp4')

ret, frame = cap.read()

box = cv2.selectROI("Select", frame, False)
cv2.destroyWindow("Select")

tracker = cv2.TrackerCSRT_create()
tracker.init(frame, box)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, box = tracker.update(frame)

    if success:
        x_axis, y_axis, width, height = [int(v) for v in box]
        cv2.rectangle(frame, (x_axis, y_axis), 
                      (x_axis+width, y_axis+height), 
                      (0,255,0), 
                      2)
    else:
        cv2.putText(frame, "Lost", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
