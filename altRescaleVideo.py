import cv2 as cv

# this is an alternate way to alter resolution(dimensions) of Live Video ONLY
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
# h
capture = cv.VideoCapture("videos/sample2.mp4")

while True:
    idTrue, frame = capture.read()

    frame_resized = capture.read()