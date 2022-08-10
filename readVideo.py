# import the necessary libraries
import cv2 as cv

# video is "captured" and stored in videocapture variable
videocapture = cv.VideoCapture("videos/sample.mp4")

# loop to read each frame successfully
while True:
    # videocapture returns: 
    # 1- a boolean for successful/failed read of a frame
    # 2- the frame that was read 
    isTrue, frame = videocapture.read()

    # creates a window to display video in
    cv.imshow("Video", frame)

    # waits for user input to end video
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

# release memory?
videocapture.release()

# lazy way to terminate everything
cv.destroyAllWindows()