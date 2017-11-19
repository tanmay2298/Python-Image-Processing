# BRIEF
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = '/Users/tanmaygulati/Documents/MATLAB/Image-Processing-using-Matlab/Retinal Scan Work/retina_scan.jpg'
img = cv2.imread(filename, 0)

# Initiate STAR detector
star = cv2.FeatureDetector_create("STAR")

# Initiate BRIEF extractor
brief = cv2.DescriptorExtractor_create("BRIEF")

# find the keypoints with STAR
kp = star.detect(img,None)

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print brief.getInt('bytes')
print des.shape