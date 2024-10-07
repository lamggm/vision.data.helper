import os
import requests
from serpapi import GoogleSearch

# Função para baixar imagens usando a API SerpApi
def download_images(query, total_count=400, output_directory=r'**********************YOUR DIR HERE**********************'):
    api_key = "**********************YOUR KEY HERE**********************"
    images_per_request = 100
    downloaded = 0
    start = 0

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    while downloaded < total_count:
        params = {
            "engine": "google",
            "q": query,
            "tbm": "isch", 
            "num": images_per_request,
            "start": start, 
            "api_key": api_key
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
                
                img_name = os.path.join(output_directory, f"{downloaded + 1}.jpg")
                
                with open(img_name, "wb") as img_file:
                    img_file.write(img_data)
                
                downloaded += 1
                print(f"Baixada: {img_name}")
                
                if downloaded >= total_count:
                    break
            except Exception as e:
                print(f"Erro ao baixar imagem {img_url}: {e}")

        start += images_per_request

download_images("**********************YOUR SEARCH HERE**********************", total_count=100)
