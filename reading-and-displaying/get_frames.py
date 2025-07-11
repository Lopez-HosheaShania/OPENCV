import cv2

# Create video capture object
capture = cv2.VideoCapture('videos/bibimbap.mp4')
 
# Check video if not open
if not capture.isOpened():
  print("Error opening video file")
 
else:
  # Get video properties and print them
  frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
  frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
  fps = capture.get(cv2.CAP_PROP_FPS)
 
  print("Image frame width: ", int(frame_width))
  print("Image frame height: ", int(frame_height))
  print("Frame rate: ", int(fps))
 
while True:
  # Read an image frame
  ret, frame = capture.read()
 
  cv2.imshow('Displaying image frames from video file', frame)
 
  if cv2.waitKey(20) & 0xFF == ord('q'):
        break
 
capture.release()
cv2.destroyAllWindows()