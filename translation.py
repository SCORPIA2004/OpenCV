import cv2 as cv
import numpy as np

img = cv.imread("photos/office.jpg")

# translation is shifting image along x-axis and y-axis

def translate(img, x, y):
    transMat = np.float32([[1, 0, x],[0, 1, y]])
    # img.shape[1] --> width
    # img.shape[0] --> height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# x --> Right
# y --> Down
# -x --> Left
# -y --> Up

img = translate(img, -200, 50)

cv.imshow("office", img)
cv.waitKey(0)