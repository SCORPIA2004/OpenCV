import cv2 as cv
import numpy as np

blank = np.zeros((800, 1000, 3), dtype="uint8")

position = (0,300)
cv.putText(blank, "hello opencv", position, cv.FONT_HERSHEY_TRIPLEX, 10.0, (0, 0, 255))
cv.imshow("Text", blank)

cv.waitKey(0)