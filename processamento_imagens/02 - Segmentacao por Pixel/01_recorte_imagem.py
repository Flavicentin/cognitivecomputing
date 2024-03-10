import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/drone.jpg"), cv2.COLOR_BGR2RGB)
plt.imshow(image, cmap="grey")
plt.show()

image2 = image[50:250, 580:950]

plt.imshow(image2, interpolation="none", cmap="gray")
plt.show()
