import cv2

# Load the pre-trained Haar cascade XML file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load your image
image = cv2.imread('Images/pic8.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load.")
    exit()
    
resize = cv2.resize(image, (1280, 720))
# Convert to grayscale
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)


# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=9
)

# Draw rectangles around detected faces
for (x_axis, y_axis, width, height) in faces:
    cv2.rectangle(resize, (x_axis, y_axis), 
                  (x_axis+width, y_axis+height), 
                  (0, 255, 0), 
                  2)

# Show the result
cv2.imshow('Detected Faces', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
