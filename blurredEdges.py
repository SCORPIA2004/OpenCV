import cv2 as cv
import numpy as np

img = cv.imread("photos/office.jpg")

# convert to blur - reduces noise in image by appyling a slight blur
blur_factor = 7
kernel_size = (blur_factor, blur_factor)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

# Edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow("CannyBlur", canny)

cv.waitKey(0)
# cv.imshow("Image", img)
# cv.imshow("Blur", blur)