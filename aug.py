import os
import shutil
import imgaug.augmenters as iaa
import cv2

# Caminhos para as pastas de treino, validação e teste
data_dirs = {
    'train': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\train',
    'valid': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\valid',
    'test': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\test'
}

# Definindo a sequência de aumentação de dados
seq = iaa.Sequential([
    iaa.Fliplr(0.5),  # Flip horizontal com probabilidade de 50%
    iaa.Affine(rotate=(-25, 25)),  # Rotacionar entre -25 e 25 graus
    iaa.Multiply((0.8, 1.2))  # Alterar brilho
])

# Função para aumentar uma imagem
def augment_image(image):
    return seq(image=image)

# Função para aumentar os dados mantendo a estrutura e salvando na mesma pasta
def augment_data(data_dir):
    image_dir = os.path.join(data_dir, 'images')
    label_dir = os.path.join(data_dir, 'labels')

    # Aumentar cada imagem e copiar a label correspondente
    for img_file in os.listdir(image_dir):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            img_path = os.path.join(image_dir, img_file)
            label_path = os.path.join(label_dir, img_file.replace('.jpg', '.txt').replace('.png', '.txt'))
            
            # Carregar imagem
            image = cv2.imread(img_path)
            
            # Aumentar imagem
            augmented_image = augment_image(image)
            
            # Gerar novo nome para a imagem aumentada
            aug_img_filename = f"aug_{img_file}"
            aug_img_path = os.path.join(image_dir, aug_img_filename)
            
            # Salvar imagem aumentada na mesma pasta
            cv2.imwrite(aug_img_path, augmented_image)
            
            # Copiar a label correspondente com o novo nome
            aug_label_path = os.path.join(label_dir, f"aug_{img_file.replace('.jpg', '.txt').replace('.png', '.txt')}")
            shutil.copy(label_path, aug_label_path)
            
            # Feedback no console
            print(f"Imagem aumentada salva: {aug_img_path}")
            print(f"Label copiada: {aug_label_path}")

# Aplicar a técnica nas pastas train, valid e test
for split in ['train', 'valid', 'test']:
    print(f"\nProcessando diretório: {split}")
    augment_data(data_dirs[split])
    print(f"Processamento do diretório {split} completo!\n")

print("Aumento de dados completo!")
