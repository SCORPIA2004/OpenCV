import cv2 as cv
import numpy as np

img = cv.imread("photos/office.jpg")

    # code goes here

cv.imshow("office", img)
cv.waitKey(0)