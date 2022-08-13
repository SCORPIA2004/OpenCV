import cv2 as cv

img = cv.imread("photos/office.jpg")



cv.imshow("office", img)
cv.waitKey(0)