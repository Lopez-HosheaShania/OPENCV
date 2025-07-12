import cv2 as cv

image = cv.imread("Images/pic2.jpg")
cv.imshow('image', image)

#-----------GRAYSCALE CONVERTION------------
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_image)

#-----------BLURRING IMAGE-------------------
blur_image = cv.GaussianBlur(image, (11, 11), 20)
cv.imshow('blur', blur_image)

#-----------EDGE DETECTION---------------------
edge_image = cv.Canny(image, 125, 175)
cv.imshow('edge', edge_image)

#-----------DILATE IMAGE------------------
dilated_image = cv.dilate(edge_image, (21,21), iterations=2)
cv.imshow('dilated', dilated_image)

#------------ERODE IMAGE-------------------
eroded_image = cv.erode(dilated_image, (21,21), iterations=2)
cv.imshow('erode', eroded_image)

#------------RESIZE IMAGE-------------------
resized_image = cv.resize(image, (1920,1080), interpolation=cv.INTER_AREA)
cv.imshow('resize', resized_image)

# ------------CROP IMAGE---------------------
cropped_image = image[1000:1500, 1500:2000]
cv.imshow('crop', cropped_image)

cv.waitKey(0)