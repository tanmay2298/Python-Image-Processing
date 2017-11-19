# SIFT
import cv2
import numpy as np

filename = '/Users/tanmaygulati/Documents/MATLAB/Image-Processing-using-Matlab/Retinal Scan Work/retina_scan.jpg'
img = cv2.imread(filename)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imwrite('sift_keypoints.jpg',img)