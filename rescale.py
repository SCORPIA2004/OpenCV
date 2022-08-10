import cv2 as cv

# rescale function by scale value
def rescaleFrame(frame, scale=0.75):
    
    # define dimensions to be resized
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    # set new dimensions
    dimensions = (width,height)

    # function to resize frame
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("photos/cat.png")
img_resized = rescaleFrame(img)
img_resized_2 = rescaleFrame(img, scale=0.2)
cv.imshow("cat", img)
cv.imshow("cat_r", img_resized)
cv.imshow("cat_r_2", img_resized_2)

cv.waitKey(0)