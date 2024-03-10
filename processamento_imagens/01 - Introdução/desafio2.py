'''
Eita! alguma está errada nesse plot, era esperado uma imagem na escala de cinza. Por que apareceu isso, como corrigir?
'''

# Coloque aqui sua solução.
import cv2
import numpy as np

from matplotlib import pyplot as plt


# Carregando a imagem na versão tons de cinza (grayscale) de um arquivo
imagem_cinza = cv2.imread("./assets/img3x3.png", 0)

plt.imshow(imagem_cinza, cmap='gray')

plt.axis('off')
plt.show()
