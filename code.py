#This is the python program for doing geomteric transformation of image
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
img = cv2.imgread('D:\Arrow.jpg')   #choose your directory and image Accordingly
rows,cols,ch = img.shape
pts1=np.float32([[50,60],[360,50],[30,390],[390,400]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])

M=cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
