#Vamos tentar fazer o contrario, vamos tentar filtar o fundo da imagem sem o drone
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("./assets/drone.jpg")
image = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
print(image.shape)

for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        print(image[x, y])
        if image[y, x, 1] < 75:
            image[y, x] = (255, 255, 255)

plt.imshow(image, interpolation="none")
plt.show()
