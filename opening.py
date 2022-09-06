import matplotlib.pyplot as plt
import cv2
import numpy as np
img = cv2.imread('image.png')
kernel = np.ones((5, 5), np.uint8)
kernel1 = np.array([[1, -1, 1], [-1, 4, -2], [-1, -1, 1]])
kernel2 = np.array([[1, -1], [-1, 4]])
grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
img_erosion = cv2.erode(binary, kernel, iterations=1)
img_erosion1 = cv2.erode(binary, kernel1, iterations=1)
img_erosion2 = cv2.erode(binary, kernel2, iterations=1)
img_dilation = cv2.dilate(binary, kernel, iterations=1)
img_dilation1 = cv2.dilate(binary, kernel1, iterations=1)
img_dilation2 = cv2.dilate(binary, kernel2, iterations=1)
plt.imshow(img_dilation,cmap='gray')
plt.show()
