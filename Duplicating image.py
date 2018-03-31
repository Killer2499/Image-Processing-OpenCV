import numpy as np
import cv2

img = cv2.imread('goku.png',cv2.IMREAD_COLOR)

px=img[55,55]#Getting colors from certain point

print(px)
img[100:150,100:150]=(255,255,255)

watch_face=img[37:111,107:194]#get values to clone..
img[0:74,0:87]=watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
