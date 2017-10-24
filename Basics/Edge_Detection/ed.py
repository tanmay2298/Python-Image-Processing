import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    check, frame = cap.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    cv2.imshow("Original", frame)
    cv2.imshow("laplacian", laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    # key == cv2.waitKey(1)
    # if key==ord('q'):
    #     break
cv2.destroyAllWindows()
cap.release()
