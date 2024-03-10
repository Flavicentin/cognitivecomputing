import requests

# URLs das imagens que você deseja baixar
urls = [
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/cogumelo.png",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/droneinvertido.jpg",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/drone.jpg",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/droneinvertido.jpg",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/goku.jpg",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/gokuinvertido.jpg",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab02/cogumelo.png"
]

dest_folder = "assets"

for url in urls:
    file_name = url.split("/")[-1]
    dest_path = f"{dest_folder}/{file_name}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(response.content)
        print(f"Imagem {file_name} baixada com sucesso!")
    else:
        print(f"Erro ao baixar a imagem {file_name}: {response.status_code}")
