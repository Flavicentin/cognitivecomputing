"""
A imagem foi dividida em 4 quadrantes aleatorios e precisamos organizar essa bagunça. Faça a reconstrução da imagem nas
posições corretas.

Dica: Crie uma copia da imagem original (img2 = img.copy()), faça um crop da imagem 4 partes
(crop1, crop2, crop3, crop4), junte as partes cortadas na ordem correta na img2. no final Salve a imagem (cv2.imwrite())
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/gokuinvertido.jpg"), cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.show()

img1 = image[0:360, 0:640]
img2 = image[0:360, 640:1280]
img3 = image[360:720, 0:640]
img4 = image[360:720, 640:1280]

part1 = np.hstack((img4, img3))
part2 = np.hstack((img2, img1))

finalImage = np.vstack((part1, part2))
plt.imshow(finalImage)
plt.show()
