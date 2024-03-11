import requests

# URLs das imagens que você deseja baixar
urls = [
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab03/bola.png",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab03/bolinha.png",
    "https://raw.githubusercontent.com/arnaldojr/cognitivecomputing/master/material/aulas/PDI/lab03/fuca.png"
]

# Pasta de destino onde você deseja salvar as imagens
dest_folder = "assets"

# Iterar sobre as URLs e baixar as imagens
for url in urls:
    # Extrair o nome do arquivo da URL
    file_name = url.split("/")[-1]
    # Criar o caminho completo do arquivo de destino
    dest_path = f"{dest_folder}/{file_name}"
    # Fazer a solicitação GET para baixar a imagem
    response = requests.get(url)
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Salvar a imagem no disco
        with open(dest_path, "wb") as f:
            f.write(response.content)
        print(f"Imagem {file_name} baixada com sucesso!")
    else:
        print(f"Erro ao baixar a imagem {file_name}: {response.status_code}")
