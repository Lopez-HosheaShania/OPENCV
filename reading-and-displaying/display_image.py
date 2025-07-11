import cv2

image = cv2.imread('photos/cat.jpg')
# orig_image = cv2.imread('photos/cat.jpg')

if image is None:
    print("Error: Failed to load the image. Check the file path or format.")
else:
    print("Image loaded successfully!")

cv2.imshow('Cat Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()