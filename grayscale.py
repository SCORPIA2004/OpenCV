import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.png")

# convert to grayscale - allows us to see intensity distribution
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Cat", img)
cv.imshow("gray", gray)
cv.waitKey(0)