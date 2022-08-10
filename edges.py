import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# create edge cascades - finds the edges present in image, using canny edges
canny = cv.Canny(img, 125, 175)

cv.imshow("Image", img)
cv.imshow("Canny", canny)

cv.waitKey(0)