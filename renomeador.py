import os

pasta = r'**********************YOUR DIR HERE**********************'

arquivos = os.listdir(pasta)

arquivos.sort()

arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(pasta, arquivo))]

for i, arquivo in enumerate(arquivos, start=1):
    temp_nome = f'_temp_{i}{os.path.splitext(arquivo)[1]}'

    caminho_antigo = os.path.join(pasta, arquivo)
    caminho_temp = os.path.join(pasta, temp_nome)

    os.rename(caminho_antigo, caminho_temp)

temporarios = os.listdir(pasta)
temporarios.sort()

for i, arquivo in enumerate(temporarios, start=1):
    novo_nome = f'a{i}{os.path.splitext(arquivo)[1]}'

    caminho_temp = os.path.join(pasta, arquivo)
    caminho_final = os.path.join(pasta, novo_nome)

    os.rename(caminho_temp, caminho_final)

print(f"Done.")
