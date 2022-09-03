import cv2 as cv
import numpy as np

img = cv.imread("photos/corp.jpg")

# visualise the contours found in image by drawing them over the image
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blank)


# convert to grayscale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# USE THRESHOLD method to help detect contours
ret, img = cv.threshold(img, 125, 255, cv.THRESH_BINARY)

# find contours
    # kinds of RETR:
        #       RETER_TREE --> returns only all hierarchical countours
        #       RETER_EXTERNAL --> returns only all external countours
        #       RETER_LIST --> returns all countours

contours, hierarchies = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f"num of contours found: {len(contours)}")



cv.imshow("image", img)
cv.waitKey(0)