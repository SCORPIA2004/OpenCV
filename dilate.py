import cv2 as cv
import numpy as np

img = cv.imread("photos/office.jpg")

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilation of structuring element(canny in this case)
dilate_factor = 9
kernel_size = (dilate_factor, dilate_factor)
dilate = cv.dilate(canny, kernel_size, iterations=3)

cv.imshow("Dilated", dilate)

cv.waitKey(0)