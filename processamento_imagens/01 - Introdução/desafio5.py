"""
Crie uma array de zero com 8 linhas e 5 colunas. E escreva (desenhe) a primeira letra do seu nome ou grupo.

Plot a imagem para visualizar o resultado.
Dica: Use np.zeros() para criar o array, para facilitar faça em escala de cinza onde o valor de intensidade
do pixel 0=branco e 255=preto.

"""
import numpy as np
from matplotlib import pyplot as plt

letra = np.zeros((8, 5), dtype=int)
print(letra)
plt.imshow(letra, cmap="gray")
plt.show()

letra[1:3, 1:4] = 255
plt.imshow(letra, cmap="gray")
plt.show()

letra[3:4, 1:4] = 255
plt.imshow(letra, cmap="gray")
plt.show()

letra[4:8, 1:4] = 255
plt.imshow(letra, cmap="gray")
plt.show()
