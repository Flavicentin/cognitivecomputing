'''
Abra a imagem "img3x3.png" e plote suas componentes externas (shape) e internas (matriz).

Como você esta relacionado as possições da matriz com os pixels da imagem??

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = "./assets/img3x3.png"

image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)

print(image)

print(image.shape)

plt.imshow(image, interpolation="none")
plt.show()


