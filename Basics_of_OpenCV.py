#importing useful libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#loading in the image
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

#converted to grayscale, therefore it consists only of one channel
img.shape

#displaying image in a window
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plotting the image in the notebook
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

#save image to file (e.g. after preprocessing)
cv2.imwrite('watchgray.jpg',img)

