import numpy as np
import cv2

b = np.zeros([400,400],dtype = 'uint8')

for i in range(40,320,80):
    for j in range(40,320,80):
        b[j-40:j,i-40:i] = 255
        b[j:j+40,i:i+40] = 255

cv2.imshow('CheckerBoard 8 * 8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
