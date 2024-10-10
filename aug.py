import os
import shutil
import imgaug.augmenters as iaa
import cv2

data_dirs = {
    'train': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\train',
    'valid': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\valid',
    'test': r'C:\Users\lamgg\Downloads\D Vision.v4i.yolov11\test'
}

seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.Affine(rotate=(-25, 25)),
    iaa.Multiply((0.8, 1.2))
])

def augment_image(image):
    return seq(image=image)

def augment_data(data_dir):
    image_dir = os.path.join(data_dir, 'images')
    label_dir = os.path.join(data_dir, 'labels')

    for img_file in os.listdir(image_dir):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            img_path = os.path.join(image_dir, img_file)
            label_path = os.path.join(label_dir, img_file.replace('.jpg', '.txt').replace('.png', '.txt'))
            
            image = cv2.imread(img_path)
            
            augmented_image = augment_image(image)
            
            aug_img_filename = f"aug_{img_file}"
            aug_img_path = os.path.join(image_dir, aug_img_filename)
            
            cv2.imwrite(aug_img_path, augmented_image)
            
            aug_label_path = os.path.join(label_dir, f"aug_{img_file.replace('.jpg', '.txt').replace('.png', '.txt')}")
            shutil.copy(label_path, aug_label_path)
            
            print(f"Imagem aumentada salva: {aug_img_path}")
            print(f"Label copiada: {aug_label_path}")

for split in ['train', 'valid', 'test']:
    print(f"\nProcessando diretório: {split}")
    augment_data(data_dirs[split])
    print(f"Processamento do diretório {split} completo!\n")

print("Aumento de dados completo!")
