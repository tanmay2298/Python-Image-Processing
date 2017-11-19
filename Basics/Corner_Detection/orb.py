# ORB
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = '/Users/tanmaygulati/Documents/MATLAB/Image-Processing-using-Matlab/Retinal Scan Work/retina_scan.jpg'
img = cv2.imread(filename, 0)

# Initiate STAR detector
orb = cv2.ORB()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()