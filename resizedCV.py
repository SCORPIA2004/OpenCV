import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# resize image to smaller dimensions
size = 500
final_dimensions = (size, size)
resize = cv.resize(img, final_dimensions, interpolation=cv.INTER_AREA)

# resize to bigger dimensions - INTER_LINEAR
size = 1000
final_dimensions = (size, size)
resize_big = cv.resize(img, final_dimensions, interpolation=cv.INTER_LINEAR)

# resize to bigger dimensions - INTER_CUBIC
size = 1000
final_dimensions = (size, size)
resize_big2 = cv.resize(img, final_dimensions, interpolation=cv.INTER_CUBIC)



cv.imshow("Original", img)
# cv.imshow("Resized", resize)
cv.imshow("Resized_Big", resize_big)
cv.imshow("Resized_Big2", resize_big2)

cv.waitKey(0)