import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# previously to resize we did this:
final_size = (500, 500)
# make smaller
resized = cv.resize(img, final_size, interpolation=cv.INTER_AREA)   
# resized = cv.resize(img, final_size, interpolation=cv.INTER_CUBIC)   <-- make Bigger



cv.imshow("corp", resized)
cv.waitKey(0)