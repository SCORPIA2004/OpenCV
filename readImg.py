# import the necessary libraries
import cv2 as cv

# read and store image at path to  img variable
img = cv.imread('photos/cat.png')

# creates a window to display image
cv.imshow('Cat', img)

# awaits '0' keypress which terminates program
cv.waitKey(0)