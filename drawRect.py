import cv2 as cv
import numpy as np

# makes a blank canvas of (width, height, numOfColors), dtype="uint8" 
blank = np.zeros((500,500, 3), dtype="uint8")

# declares color variable
color = (0, 255, 0)
widthOfWindow = blank.shape[1]
heightOfWindow = blank.shape[0]

#           (window, coordinates of left-top corner of shape, dimensions, color, thickness)
cv.rectangle(blank, (100,0), (widthOfWindow // 2, heightOfWindow // 2), color, thickness=2)

# plot this on canvas
cv.imshow("B rectangle", blank)

cv.waitKey(0)
