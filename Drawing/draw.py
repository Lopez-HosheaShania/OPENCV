import cv2 as cv
import numpy

# displays black image
# height and width is 500 with 3 color channel
blank_image = numpy.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow("blank", blank_image)

#----------------Color------------------------
#adding color to the blank image
#by default, it is blue-green-red
blank_image[:] = 255, 255, 255

# adding color to a specific area only
blank_image[200:300, 200:300] = 255, 255, 255
cv.imshow('color', blank_image)

#-----------------Rectangle-------------------
# #draw a rectangle
# #(image, point1, point2, color, thickness)
# cv.rectangle(blank_image, (100,200), (200,100), (255,0,0), thickness = 10 )
# cv.imshow('rectangle', blank_image)

# #-------------------Circle--------------------
# #draw a circle
# #(image, center_point, pixel_radius, color, thickness)
# cv.circle(blank_image, (250,250), 40, (255,0,0), thickness=10)
# cv.imshow('circle', blank_image)

# #-------------------Line----------------------
#draw a line
#(image, starting_point, end_point, color, thickness)
# cv.line(blank_image, (0,0), (300,300), (255,0,0), thickness=10)
# cv.line(blank_image, (200,0), (400,400), (255,0,0), thickness=10)
# cv.imshow('line', blank_image)

# #--------------------Text----------------------
#write a text
#(image, 'text', starting_point, font, font_scale, color, thickness)
# cv.putText(blank_image, 
#         'Hello World', 
#         (200,400), 
#         cv.FONT_HERSHEY_SIMPLEX, 
#         1, 
#         (255,255,0), 
#         5)

cv.imshow('draw', blank_image)
cv.waitKey(0)