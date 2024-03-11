import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("./assets/fuca.png"), cv2.COLOR_BGR2GRAY)

plt.imshow(img, cmap="Greys_r", vmin=0, vmax=255)
plt.show()

plt.hist(img.ravel(), 256, [0, 256])
plt.show()

img_eq = cv2.equalizeHist(img)
plt.imshow(3*img_eq, cmap="Greys_r", vmin=0, vmax=255)
plt.show()

plt.hist(3*img_eq.ravel(),256,[0,256])
plt.show()
