'''
Implemente um codigo que faz a alteração do pixel(0,0) para a a cor Magenta - RGB (255,0,255);
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/img3x3.png"), cv2.COLOR_BGR2RGB)

image[0, 0, 0] = 255
image[0, 0, 1] = 0
image[0, 0, 2] = 255

plt.imshow(image)
plt.show()
