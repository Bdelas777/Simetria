from cryptography.fernet import Fernet
from PIL import Image

# Función para cifrar una imagen
def cifrar_imagen(ruta_imagen, clave, ruta_salida):
    # Leer los bytes de la imagen desde el archivo
    with open(ruta_imagen, "rb") as f:
        bytes_imagen = f.read()

    # Crear un objeto Fernet con la clave proporcionada
    fernet = Fernet(clave)

    # Cifrar los bytes de la imagen
    bytes_cifrados = fernet.encrypt(bytes_imagen)

    # Escribir los bytes cifrados en un nuevo archivo de salida
    with open(ruta_salida, "wb") as f:
        f.write(bytes_cifrados)

# Función para descifrar una imagen
def descifrar_imagen(ruta_imagen, clave, ruta_salida):
    # Leer los bytes cifrados de la imagen desde el archivo
    with open(ruta_imagen, "rb") as f:
        bytes_cifrados = f.read()

    # Crear un objeto Fernet con la clave proporcionada
    fernet = Fernet(clave)

    # Descifrar los bytes de la imagen
    bytes_descifrados = fernet.decrypt(bytes_cifrados)

    # Escribir los bytes descifrados en un nuevo archivo de salida
    with open(ruta_salida, "wb") as f:
        f.write(bytes_descifrados)

# Función principal que actúa como un menú de consola
def main():
    print("1. Cifrar Imagen")
    print("2. Descifrar Imagen")
    
    # Solicitar al usuario que elija entre cifrar y descifrar
    eleccion = input("Ingrese su elección (1 o 2): ")

    # Generar una nueva clave Fernet
    clave = Fernet.generate_key()

    if eleccion == "1":
        # Cifrar una imagen
        ruta_imagen = input("Ingrese la ruta de la imagen: ")
        ruta_salida = input("Ingrese la ruta para la imagen cifrada: ")
        cifrar_imagen(ruta_imagen, clave, ruta_salida)
        print("Imagen cifrada exitosamente.")
    elif eleccion == "2":
        # Descifrar una imagen
        ruta_imagen = input("Ingrese la ruta de la imagen cifrada: ")
        ruta_salida = input("Ingrese la ruta para la imagen descifrada: ")
        descifrar_imagen(ruta_imagen, clave, ruta_salida)
        print("Imagen descifrada exitosamente.")
    else:
        print("Elección no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()

'''
No me salio el codigo pero aqui estan las fuentes
https://es.stackoverflow.com/questions/222412/python-c%c3%b3mo-encripto-archivos-usando-aes-crypto-cipher

edgeservices.bing.com/edgesvc/redirect?url=https%3A%2F%2Fhashdork.com%2Fes%2Fcifrado-de-archivos-descifrado-usando-python%2F&hash=68245Xz2imXrvBW%2FDXzlE34BqYHTLf4vOTUsZ9sh244%3D&key=psc-underside&usparams=cvid%3A51D%7CBingProd%7CCDB65FB0C36EDECB58E9B8AEFD272DFE6C8CA3AC839A220BDC09A704CBF3A36D%5Ertone%3ABalanced

https://medium.com/@FridaRuh/encriptar-y-desencriptar-datos-en-pyhon-con-cryptography-5b186c669801
'''