import cv2 as cv
import numpy as np

# makes a blank canvas of (width, height, numOfColors), dtype="uint8" 
blank = np.zeros((500,500, 3), dtype="uint8")


blank[100:300, 300:400] = 255, 0, 0
cv.imshow("B", blank)

cv.waitKey(0)