# Importando a biblioteca OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt

imageNature = "./assets/NATUREZA_1.jpg"

image_rgb = cv2.cvtColor(cv2.imread(imageNature), cv2.COLOR_BGR2RGB)

print("Dimensões da imagem: ", image_rgb.shape)
print("Quantidade de linhas: ", image_rgb.shape[0])
print("Quantidade de colunas: ", image_rgb.shape[1])
print("Camadas de cores: ", image_rgb.shape[2])

plt.imshow(image_rgb, interpolation="none")
plt.show()
