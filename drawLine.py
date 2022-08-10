import cv2 as cv
import numpy as np
import time

# makes a blank canvas of (width, height, numOfColors), dtype="uint8" 
blank = np.zeros((830,1520, 3), dtype="uint8")

# declares color variable
color = (0, 0, 255)
# widthOfWindow
w = blank.shape[1]
# heightOfWindow
h = blank.shape[0]


# draw line
maxh = h + 10
maxw = w + 10
step = 50

for i in range(0, maxw, step):
    cv.line(blank, (i, 0), (w // 2, h // 2), color, thickness=2)
for j in range(0, maxh, step):
    cv.line(blank, (0, j), (w // 2, h // 2), color, thickness=2)
    
for k in range(0, maxw, step):
    cv.line(blank, (k, h), (w // 2, h // 2), color, thickness=2)
for l in range(0, maxh, step):
    cv.line(blank, (w, l), (w // 2, h // 2), color, thickness=2)

for i in range(20, w, step):
    cv.circle(blank, (w // 2, h // 2), i, color, thickness=2)


# plot this on canvas
cv.imshow("B rectangle", blank)
cv.waitKey(0)
