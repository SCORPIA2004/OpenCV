import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

    # code goes here

cv.imshow("corp", img)
cv.waitKey(0)