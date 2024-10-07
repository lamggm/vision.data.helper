import os

# Caminho da pasta onde estão os arquivos
pasta = r'C:\Users\lamgg\Documents\GitHub\vision\Treinamento\dataset\Riscos'

# Listar todos os arquivos na pasta
arquivos = os.listdir(pasta)

# Ordenar os arquivos
arquivos.sort()

# Filtrar apenas os arquivos (ignorando subpastas, por exemplo)
arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(pasta, arquivo))]

# Etapa 1: Renomear todos os arquivos para um nome temporário, evitando conflitos
for i, arquivo in enumerate(arquivos, start=1):
    # Criar um nome temporário único (prefixo _temp_)
    temp_nome = f'_temp_{i}{os.path.splitext(arquivo)[1]}'  # Preserva a extensão original

    # Caminho completo do arquivo antigo e do nome temporário
    caminho_antigo = os.path.join(pasta, arquivo)
    caminho_temp = os.path.join(pasta, temp_nome)

    # Renomear o arquivo para o nome temporário
    os.rename(caminho_antigo, caminho_temp)

# Etapa 2: Renomear dos temporários para o formato final 'a1', 'a2', etc.
temporarios = os.listdir(pasta)
temporarios.sort()

for i, arquivo in enumerate(temporarios, start=1):
    # Criar o novo nome no formato 'a1', 'a2', 'a3', etc.
    novo_nome = f'a{i}{os.path.splitext(arquivo)[1]}'  # Preserva a extensão original

    # Caminho completo do arquivo temporário e do novo nome
    caminho_temp = os.path.join(pasta, arquivo)
    caminho_final = os.path.join(pasta, novo_nome)

    # Renomear o arquivo temporário para o nome final
    os.rename(caminho_temp, caminho_final)

print(f"Todos os arquivos foram renomeados para garantir que não existam lacunas na sequência.")
