### seu código aqui
import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = np.zeros((50, 50), dtype=int)

print(imagem.shape[0])
meio = int(imagem.shape[1] / 2)
print(meio)
for y in range(0, int(imagem.shape[0])):
    for x in range(meio - 1, meio + 1):
        imagem[y, x] = 255

plt.imshow(imagem, cmap="gray")
plt.show()
