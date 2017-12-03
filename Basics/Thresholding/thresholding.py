import cv2
import numpy as np

img = cv2.imread("retina_scan.jpg");
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imwrite("Thresholded_retina.jpg", threshold)
cv2.imshow('original', img)
cv2.imshow('threshold original', threshold)
cv2.imshow('threshold grayscale',threshold2)
cv2.imshow('Gaus',gaus)
cv2.imwrite("Gaus.png", gaus)
cv2.imshow('Otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
