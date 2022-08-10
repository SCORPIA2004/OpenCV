import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

dilate_factor = 5
dilate_kernel_size = (dilate_factor, dilate_factor)
dilate = cv.dilate(canny, dilate_kernel_size, iterations=3)

cv.imshow("Dilated", dilate)

# eroding dilated image to convert it back to canny image
erode_factor = 5
erode_kernel_size = (erode_factor, erode_factor)
erode = cv.erode(dilate, erode_kernel_size, iterations=3)

cv.imshow("Eroded", erode)

cv.waitKey(0)