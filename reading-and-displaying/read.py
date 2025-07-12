import cv2 as cv
from readmodules import rescale

#--------------Image Capture-----------------
# #returns as a matrix of pixels
# image = cv.imread('Images/pic4.jpg')

# rescaled_image = rescale.rescaleFrame(image, 0.1)

# #display image in a seperate window
# cv.imshow('pic1', image)

# #display rescaled image in a seperate window
# cv.imshow('rescale pic1', rescaled_image)

# #keyboard binding function that waits for a pressed key
# cv.waitKey(0)

#--------------Video Capture-----------------

# capture = cv.VideoCapture('Videos/vid1.mp4')

# while True:
#     # reads the video frame by frame 
#     # and a bolean that will tell if the video has been read or not
#     isTrue, frame = capture.read()
    
#     rescaled_video = rescale.rescaleFrame(frame, 0.3)
    
#     # displays the video frame by frame
#     cv.imshow('Video', rescaled_video)
    
#     #to stop the video from playing indefinitely
#     if cv.waitKey(20) & 255 == ord('d'):
#         break

# #Once the video is done, it stop capturing the video and exits the window
# capture.release()
# cv.destroyAllWindows()

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv.VideoCapture(1)

while True:
    # reads the video frame by frame 
    # and a bolean that will tell if the video has been read or not
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,       # How much the image size is reduced at each image scale
    minNeighbors=8,        # How many neighbors each rectangle should have to be retained
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # displays the video frame by frame
    cv.imshow('Video', frame)
    
    #to stop the video from playing indefinitely
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    
# #------------------Get Resolution---------------------------------
# print(image.shape)

#Once the video is done, it stop capturing the video and exits the window
capture.release()
cv.destroyAllWindows()