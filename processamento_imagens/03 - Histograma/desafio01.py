"""
Faça a seguimentação da bolinha de cor laranja. Dica use 2 canais de cores para conseguir seguimentar.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/bola.png"), cv2.COLOR_BGR2RGB)

plt.hist(image.ravel(), 256, [0, 256])
plt.show()

img = image.copy()

gray_r = img[:, :, 0]
gray_g = img[:, :, 1]
gray_b = img[:, :, 2]


# pro vermelho está mais para um branco (241)
# pro verde está mais para um cinza (105)
# pro azul está mais um preto (23)

img_bola = image.copy()

for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        if gray_r[y][x] >= 240 and 104 <= gray_g[y][x] <= 105 and gray_b[y][x] <= 25:

            img_bola[y][x] = img_bola[y][x]

        else:

            img_bola = 0

plt.imshow(img_bola)
plt.show()
