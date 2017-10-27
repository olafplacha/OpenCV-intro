
# coding: utf-8

# In[2]:

#import useful libraries
import numpy as np
import cv2


# In[81]:

#reading in the image
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)


# In[82]:

img.shape


# In[83]:

#drawing a line on the img
cv2.line(img, (0,0), (100,100), (255,255,255), 10)
#drawing a rectangle on the img
cv2.rectangle(img, (30, 30), (80, 150), (0, 255, 0), 2)
#drowing a circle on the img
cv2.circle(img, (100, 50), 50, (0, 0, 255), 2)
#drowing a ploygon line
pts = np.array([[3,45],[12,45],[234,62],[134,51],[2,199]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 3)
#writing on our img
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV intro', (0,130), font, 1, (100, 150, 200), 2)
#display image
cv2.imshow('image', img)
#wait for any key to be pressed
cv2.waitKey(0)
#if any key pressed, close down all the windows
cv2.destroyAllWindows()


# In[ ]:



