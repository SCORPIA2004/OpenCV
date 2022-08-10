import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.png")

# convert to blur - reduces noise in image by appyling a slight blur
blur_factor = 9
kernel_size = (blur_factor, blur_factor)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

cv.imshow("Cat", img)
cv.imshow("gray", blur)
cv.waitKey(0)