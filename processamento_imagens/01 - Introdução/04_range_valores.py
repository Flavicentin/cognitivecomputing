import cv2
import numpy as np
from matplotlib import pyplot as plt


# Carregando a imagem na versão tons de cinza (grayscale) de um arquivo
imagem_cinza = cv2.imread("./assets/img3x3.png", cv2.IMREAD_COLOR)

print(imagem_cinza)
plt.imshow(imagem_cinza)

plt.axis('off')
plt.show()