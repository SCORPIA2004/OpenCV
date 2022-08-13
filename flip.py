import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# Flip codes:
#       0 - flips image vertically
#       1 - flips image horizontally
#      -1 - flips image horizontally + vertically
# flip_code = 0

cv.imshow("corp", img)

vertically = cv.flip(img, 0)
cv.imshow("vertically", vertically)

horizontally = cv.flip(img, 1)
cv.imshow("horizontally", horizontally)

both = cv.flip(img, -1)
cv.imshow("both", both)

cv.waitKey(0)