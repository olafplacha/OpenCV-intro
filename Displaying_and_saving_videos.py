#importing useful libraries
import cv2
import numpy as np

#capturing video from video camera
cap = cv2.VideoCapture(0)
#saving the video
out = cv2.VideoWriter('output.avi', -1, 10.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    #saving frames to out var
    out.write(frame)
    
    #break if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#releasing the camera
cap.release()
out.release()
cv2.destroyAllWindows()

