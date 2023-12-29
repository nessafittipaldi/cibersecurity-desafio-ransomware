import os
import pyaes

def decrypter_file(file_name, key):
    # Abrir o arquivo criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Descriptografar o arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Registrar o nome do arquivo descriptografado
    new_file_name = input("Digite um nome para o arquivo descriptografado: ")

    # Criar o arquivo descriptografado
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"\nDescriptografia bem-sucedida. Arquivo descriptografado salvo como: {new_file_name}\n")

    # Oferecer opção para visuaslizar o arquivo descriptografado
    view_option = input("Deseja visualizar o conteúdo do arquivo descriptografado? (S/N): ")
    if view_option.lower() == 's':
        try:
            with open(new_file_name, 'r') as view_file:
                content = view_file.read()
                print(f"\nConteúdo do arquivo descriptografado:\n{content}")
        except Exception as e:
            print(f"Erro ao tentar visualizar o conteúdo do arquivo: {str(e)}")

if __name__ == "__main__":
    print('''
    ==============================================================
    ||								||
    ||			  DECRYPTER 2.0				||
    ||								||
    ==============================================================
    
    ''')
    
    # Solicita o nome do arquivo criptografado
    file_name = input("Digite o nome do arquivo criptografado: ")
    # Solicita a chave do arquivo criptografado
    key = b"testeransomwares"

    # Chama a função decrypt_file
    decrypter_file(file_name, key)
