import cv2
import numpy as np
import matplotlib.pyplot as plt

#Used to read the image
img = cv2.imread('goku.png',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv2.imshow('image',img)#Display the image
cv2.waitKey(0)#Wait unitl any keypress
cv2.destroyAllWindows()#Close the windows

#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([50,100],[80,100],'c',linewidth=5)
#plt.show()

cv2.imwrite('gokugray.png',img)#Save the file
