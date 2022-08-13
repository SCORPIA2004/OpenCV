from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# rotating image by some angle - usually done wrt to center of img, but can be specified otherwise

def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]
    dimensions = (width, height)

    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)
    rotationMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)

    return cv.warpAffine(img, rotationMat, dimensions)

# +ve angle --> anti-clockwise
# -ve angle --> clockwise

rot1 = rotate(img, -45)
rot2 = rotate(rot1, -45)

cv.imshow("corp1", rot1)
cv.imshow("corp2", rot2)
cv.waitKey(0)