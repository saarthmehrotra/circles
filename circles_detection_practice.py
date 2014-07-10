import cv2
import cv2.cv as cv
import numpy as np

img = cv2.imread('test.png',0)

img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.imshow('test.png',cimg)

circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,1,param1=100,param2=150,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    print("Center = (",i[0],i[1],")" )
    print("Radius = ", i[2])
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()