import cv2 as cv
import numpy as np
img1 = cv.imread('demo.jpg',-1)

cv.imshow('Original Image',img1)

img = cv.imread('demo.jpg',0)

cv.imshow('Image - Grayscale',img)

img2 = cv.imread('demo.jpg',1)
cv.imshow('Image - Color',img2)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                           cv.THRESH_BINARY,11,2)
cv.imshow('Image - Threshold',th2)

key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
elif key == ord('s'):
    cv.imwrite('grayimg.jpg',img)
    cv.imwrite('colorimg.jpg',img2)
    cv.imwrite('thresimg.jpg',th2)
    cv.destroyAllWindows()
