import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

# Convert BGR to HSV (for one pixel)
def bgr2hsv_pixel(b, g, r):
    color = np.uint8([[[b, g, r]]]) 
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    return hsv_color[0][0] 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV using OpenCV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set range for blue color in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Create mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            b, g, r = frame[y, x]
            h, s, v = bgr2hsv_pixel(b, g, r)
            print(f"HSV at ({x},{y}): H={h}, S={s}, V={v}")

    # Show result
    cv2.imshow("Color Tracking: Blue", frame)
    cv2.imshow("Mask", mask)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
