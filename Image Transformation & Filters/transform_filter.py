import cv2 as cv
import os
import numpy as np

root = os.getcwd()
imgpPath = os.path.join(root, r'C:\Users\Hoshea Lopez\OpenCV\DP BLAST.png')
img = cv.imread(imgpPath)

# ========== Color Space
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ========== Rotate
# rotate = cv.ROTATE_180
# # ROTATE_180
# # ROTATE_90_CLOCKWISE
# # ROTATE_90_COUNTERCLOCKWISE

# rotated_img = cv.rotate(img, rotate)

# ========== Resize
# resize_img = cv.resize(img, (1000, 600), interpolation=cv.INTER_CUBIC)
# # resize_img = rescaleFrame(img)
# # INTER_AREA - downscaling - smooth
# # INTER_CUBIC - upscaling - sharp & smooth
# # INTER_LINEAR - upscaling - smoother
# # INTER_NEAREST - speed - blocky

# ========== Grayscale
# gray_img = cv.imread(img, cv.IMREAD_GRAYSCALE)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray_img = cv.imread(img, 0)

# ========== Crop
# # Displaying Intensity Values
# cropped_img = img[30:750, 100:900, 2]

# # Visualizing Color Channels
# cropped_img = img[30:750, 100:900]

# red = cropped_img[:, :, 2]
# blue = np.zeros_like(red)
# green = np.zeros_like(red)

# # Merge as BGR image where only Red is active
# red_color_image = cv.merge([blue, green, red])

# cropped = img[y1:y2, x1:x2]

# ========== Blur
# blurred = cv2.GaussianBlur(img, ksize=(0, 0), sigmaX=2)
# median = cv2.medianBlur(img, ksize=5)
# bilateral = cv2.bilateralFilter(src, d=9, sigmaColor=75, sigmaSpace=75)

# ========== Edge Cascade
# edge = cv.Canny(img, 125, 175)

# ========== Erode
# erode = cv.erode(edge, (3,3), iterations=1)

# ========== Dilation
# dilate = cv.dilate(erode, (3,3), iterations=2)

# ========== Gradient
# # Laplacian
# laplacian = cv.Laplacian(gray_img ,cv.CV_64F)

# # Sobel Gradient
# sobelx = cv.Sobel(gray_img,cv.CV_64F,1,0,ksize=5)
# sobely = cv.Sobel(gray_img,cv.CV_64F,0,1,ksize=5)

# sobel_combined = cv.magnitude(sobelx, sobely)

cv.imshow('sample', img)

# cv.imwrite('sample.jpg', img)

cv.waitKey(0)