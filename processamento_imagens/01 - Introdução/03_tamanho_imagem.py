# cv2.resize(imagem, tamanho, interpolação)

# O tamanho é dado por uma tupla (W,H), onde W é a largura (número de colunas) e H é a altura (número de linhas)

# Carregando a imagem na versão colorida de um arquivo
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("./assets/NATUREZA_1.jpg")
image = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

print("Dimensões da imagem: ", image.shape)

tamanho = (400, 400)
interpolacao = cv2.INTER_LINEAR

imagem2 = cv2.resize(image, tamanho, interpolacao)
print("Novas dimensões da imagem: ", imagem2.shape)


plt.imshow(imagem2)
plt.show()


