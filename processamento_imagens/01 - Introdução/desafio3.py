'''
Comparar os diferentes métodos de interpolação (vizinho mais próximo, bilinear e bicúbica)
ao ampliarmos uma imagem em 10 vezes seu tamanho. Escolha uma imagem pequena.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/img3x3.png"), cv2.COLOR_BGR2RGB)

print(image.shape)

imageResize = image
interpolation = cv2.INTER_LINEAR
imageResize = cv2.resize(imageResize, (30,30), interpolation)
print(imageResize.shape)
plt.imshow(imageResize)
plt.show()

imageResize2 = image
interpolation = cv2.INTER_CUBIC
imageResize2 = cv2.resize(imageResize2, (30,30), interpolation)
print(imageResize2.shape)
plt.imshow(imageResize2)
plt.show()




