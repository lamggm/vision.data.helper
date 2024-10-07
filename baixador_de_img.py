import os
import requests
from serpapi import GoogleSearch

# Função para baixar imagens usando a API SerpApi
def download_images(query, total_count=400, output_directory=r'C:\Users\lamgg\Documents\GitHub\vision\Treinamento\dataset'):
    api_key = "16fa11d056bfd2e3ea6158750fa0e425f8d0564d77d461bbb68accd8eb9b791b"  # Insira sua chave da API SerpApi
    images_per_request = 100  # SerpApi permite até 100 imagens por requisição
    downloaded = 0
    start = 0

    # Verifica se o diretório de saída existe, caso contrário, cria
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    while downloaded < total_count:
        params = {
            "engine": "google",       # Motor de busca
            "q": query,               # Termo de busca
            "tbm": "isch",            # Tipo de busca: imagens
            "num": images_per_request, # Número de imagens por requisição (máx. 100)
            "start": start,            # Ponto de partida da próxima requisição
            "api_key": api_key        # Chave da API SerpApi
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        images_results = results.get("images_results", [])

        if not images_results:
            print("Nenhuma imagem adicional encontrada.")
            break

        for image in images_results:
            try:
                img_url = image['original']
                img_data = requests.get(img_url).content
                
                # Nome do arquivo baseado no contador (de 1 até o total desejado)
                img_name = os.path.join(output_directory, f"{downloaded + 1}.jpg")
                
                with open(img_name, "wb") as img_file:
                    img_file.write(img_data)
                
                downloaded += 1
                print(f"Baixada: {img_name}")
                
                if downloaded >= total_count:
                    break
            except Exception as e:
                print(f"Erro ao baixar imagem {img_url}: {e}")

        # Atualiza o ponto de partida para a próxima requisição
        start += images_per_request

# Baixando até 400 imagens de parafusos
download_images("scratch marks on a cabinet", total_count=100)
