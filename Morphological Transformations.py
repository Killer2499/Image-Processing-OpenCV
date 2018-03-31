import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    #hsv hue sat value
    lower_blue=np.array([ 0,150,50])
    upper_blue=np.array([180,255,150])

    #dark_blue=np.uint8([[[12,22,121]]])
    #dark_blue=cv2.cvtColor(dark_blue,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res= cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)

    opening=cv2.morphologyEx(mask,v2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,v2.MORPH_CLOSE,kernel)
    
   
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    

    k=cv2.waitKey(5) &0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()
 
