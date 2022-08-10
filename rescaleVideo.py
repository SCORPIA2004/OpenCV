import cv2 as cv

# rescale function by scale value
def rescaleFrame(frame, scale=0.75):
    
    # defines the h & w
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Read in video file
videoCapture = cv.VideoCapture("videos/sample.mp4")

# Display video
while True:
    # read frame by frame
    isTrue, frame = videoCapture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video_r", frame_resized)
    

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

videoCapture.release()

cv.destroyAllWindows()