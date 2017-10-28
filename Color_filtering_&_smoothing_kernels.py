import numpy as np
import cv2


#getting the video from webcam
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #threshold values
    lower_red1 = np.array([150,120,60])
    upper_red1 = np.array([180,255,255])
    lower_red2 = np.array([0,140,60])
    upper_red2 = np.array([10,255,255])
    #creating a mask
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    MASK = mask1 + mask2
    #applying smoothing kernel
    kernel = np.ones((15,15), np.float32)/255
    #smoothed = cv2.filter2D(res, -1, kernel)
    #applying gaussian bluring
    #blur = cv2.GaussianBlur(res, (15,15), 0)
    #applying median blur
    #median = cv2.medianBlur(res, 15)
    
    #applying erosion and dilation
    kernel1 = np.ones((5,5), np.uint8)
    kernel2 = np.ones((10,10), np.uint8)  
    erosion = cv2.erode(MASK, kernel1, iterations = 1)
    dilation = cv2.dilate(erosion, kernel2, iterations = 1)
    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
    MASK = closing
    
    #applying the mask
    res = cv2.bitwise_and(frame, frame, mask = MASK)

    
    #displaying the results
    cv2.imshow('frame', frame)
    cv2.imshow('MAKS', MASK)
    #cv2.imshow('mask1', mask1)
    #cv2.imshow('mask2', mask2)
    cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
