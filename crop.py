from calendar import c
import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

crop = img[0:200, 300:400]

cv.imshow("Cropped", crop)
cv.waitKey(0)