import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.cvtColor(cv2.imread("./assets/bola.png"), cv2.COLOR_BGR2RGB)

plt.imshow(image, vmin=0, vmax=255)
plt.show()

plt.hist(image.ravel(),256,[0,256])
plt.show()

# =============================================================
# HISTOGRAMA VERMELHO
# =============================================================
plt.imshow(image[:,:,0], cmap="gray", vmin=0, vmax=255)
plt.show()

plt.hist(image[:,:,0].ravel(),256,[0,256])
plt.show()

# =============================================================
# HISTOGRAMA VERDE
# =============================================================
plt.imshow(image[:,:,1], cmap="Greys_r", vmin=0, vmax=255)
plt.show()

plt.hist(image[:,:,1].ravel(),256,[0,256])
plt.show()

# =============================================================
# HISTOGRAMA AZUL
# =============================================================
plt.imshow(image[:,:,2], cmap="Greys_r", vmin=0, vmax=255)
plt.show()

plt.hist(image[:,:,2].ravel(),256,[0,256])
plt.show()

image2 = image.copy()
gray_r = image2[:, :, 0]
gray_g = image2[:, :, 1]
gray_b = image2[:, :, 2]

img_bola = image2.copy()

for y in range(0, image2.shape[0]):
    for x in range(0, image2.shape[1]):
        if gray_g[y][x] <= 230:
            img_bola[y][x] = 0
        if gray_b[y][x] >= 240:
            img_bola[y][x] = 0

plt.imshow(img_bola, interpolation="none")
plt.show()
