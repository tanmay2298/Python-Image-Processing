import cv2
import numpy as np
 
filename = '/Users/tanmaygulati/Documents/MATLAB/Image-Processing-using-Matlab/Retinal Scan Work/retina_scan.jpg'
filename2 = 'Gauss.jpg'
img = cv2.imread(filename2,0)
# size = np.size(img)
# skel = np.zeros(img.shape,np.uint8)
 
# ret,img = cv2.threshold(img,127,255,0)
# element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# done = False
 
# while( not done):
#     eroded = cv2.erode(img,element)
#     temp = cv2.dilate(eroded,element)
#     temp = cv2.subtract(img,temp)
#     skel = cv2.bitwise_or(skel,temp)
#     img = eroded.copy()
 
#     zeros = size - cv2.countNonZero(img)
#     if zeros==size:
#         done = True
 
# cv2.imshow("skel",skel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img = img.copy() # don't clobber original
    # skel = img.copy()
img = img.copy()
skel = img.copy()
skel[:,:] = 0
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while True:
    eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
    temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
    temp  = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img[:,:] = eroded[:,:]
    if cv2.countNonZero(img) == 0:
        break

cv2.imshow("skel",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()