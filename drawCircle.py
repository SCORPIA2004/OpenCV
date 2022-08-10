import cv2 as cv
import numpy as np

# makes a blank canvas of (width, height, numOfColors), dtype="uint8" 
blank = np.zeros((500,500, 3), dtype="uint8")

# declares color variable
color = (0, 255, 0)
widthOfWindow = blank.shape[1]
heightOfWindow = blank.shape[0]

# draw circle
for i in range(20, 200, 20):
    cv.circle(blank, (widthOfWindow // 2, heightOfWindow // 2), i, color, thickness=2)

# plot this on canvas
cv.imshow("B rectangle", blank)

cv.waitKey(0)
