'''
Faça uma implementação que inverte as cores de uma imagem em escala de cinza, com valores que vão de 0 ate 255.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/drone.jpg"), cv2.COLOR_BGR2GRAY)
plt.imshow(image, cmap="grey")
plt.show()

inverted_image = 255 - image

plt.imshow(inverted_image, cmap="grey")
plt.show()