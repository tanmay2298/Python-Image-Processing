# Shi-Tomasi Corner Detection
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 1) Retina scan
# 2) Finger print scan
# filename = '/Users/tanmaygulati/Documents/MATLAB/Image-Processing-using-Matlab/Retinal Scan Work/retina_scan.jpg'
# filename = '/Users/tanmaygulati/Work/Research Project/Dr Srikanth Prabhu/Python-Image-Processing/Basics/Corner_Detection/snap2.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imwrite("Shi-Tomasi2.png", img)
plt.imshow(img),plt.show()