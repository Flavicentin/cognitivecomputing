import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("./assets/cogumelo.png")
image = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

plt.imshow(image, interpolation="none", cmap="gray")
plt.show()

for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        if image[y, x] == 255:
            image[y, x] = 0
        else:
            image[y, x] = 255

plt.imshow(image, interpolation="none", cmap="gray")
plt.show()
