from ctypes.wintypes import RGB
import os
import cv2
from cv2 import COLOR_RGB2BGR
import numpy as np
from matplotlib import pyplot as plt

# 이미지 가져오기
img = cv2.imread("HW_02_01_image_thresholding.png")
cv2.imshow("Image", img)

# RGB split
r, g, b = cv2.split(img)

img1 = cv2.imshow("Red", r)
img2 = cv2.imshow("Green", g)
img3 = cv2.imshow("Blue", b)

# Image merge
titles = ['Original Image', 'Red Image', 'Green Image', 'Blue Image']
images = [img, img1, img2, img3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#print(img, img1, img2, img3)