import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# convert to grayscale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur_factor = 1
kernel_size = (blur_factor, blur_factor)
img = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

# get all edges using canny
img = cv.Canny(img, 125, 175)
# find contours
# kinds of RETR:
#       RETER_TREE --> returns only all hierarchical countours
#       RETER_EXTERNAL --> returns only all external countours
#       RETER_LIST --> returns all countours

contours, hierarchies = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f"num of contours found: {len(contours)}")

cv.imshow("corp", img)
cv.waitKey(0)