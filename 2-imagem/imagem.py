#Importa a biblioteca PIL, Python Image Library.
from PIL import Image
#Importar a biblioteca numérica numpy.
import numpy as np

"""
Pode ser necessário instalar as bibliotecas.
Para isso basta rodar os comandos no terminal.
pip install Pillow
pip install numpy
"""
 
def main():
    # Carregar a imagem original
    img = Image.open("simple_icon.png") #Abre o arquivo como imagem (não existe arquivo).
    img.show()
 
    # Converter a imagem em dados binários
    img_data = np.array(img) #Transforma o arquivo lido em um array.
    binary_data = img_data.tobytes()
 
    # Salvar os dados binários em um arquivo
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)
 
    # Copiar o arquivo binário
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()
    
    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)
 
    # Manipulação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())
    
    # Inverte todos os bytes
    data = data[::-1]
 
    with open("copy_img.bin", "wb") as file:
        file.write(data)
 
    # Carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()
 
if __name__ == "__main__":
    main()