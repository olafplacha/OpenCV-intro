import cv2
import numpy as np

#reading in the image
img = cv2.imread('opencv-corner-detection-sample.jpg')
#creating gray copy
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#detecting corners
corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 1)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, 1)
    
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

