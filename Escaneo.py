import os  # Para obtener la extensión de la imagen

def encrypt_image():
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")

    while not os.path.exists(ruta_imagen):
        print("La imagen no existe. Por favor, verifica la ruta e intenta nuevamente.")
        ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")

    extension = os.path.splitext(ruta_imagen)[1].upper()

    while extension not in [".JPEG", ".PNG", ".JPG"]:
        print("Por favor, ingresa una imagen con extensión .JPEG, .PNG o .JPG.")
        ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
        extension = os.path.splitext(ruta_imagen)[1].upper()

    if os.path.exists("imagen_encriptada.jpg"):
        print("La imagen ya está encriptada. Por favor, desencripta la imagen existente o elige otra imagen.")
        return

    numero = int(input("Por favor, ingresa un número (clave): "))

    with open(ruta_imagen, "rb") as file:
        image = bytearray(file.read())

    for i, j in enumerate(image):
        image[i] = j ^ numero

    with open("imagen_encriptada.jpg", "wb") as file:
        file.write(image)
    print("Imagen encriptada y guardada como 'imagen_encriptada.jpg'.")

def decrypt_image():
    if not os.path.exists("imagen_encriptada.jpg"):
        print("La imagen encriptada no existe. Por favor, encripta una imagen antes de intentar desencriptar.")
        return

    numero = int(input("Por favor, ingresa el número (clave): "))

    with open("imagen_encriptada.jpg", "rb") as file:
        image = bytearray(file.read())

    for i, j in enumerate(image):
        image[i] = j ^ numero

    with open("decrypted.jpg", "wb") as file:
        file.write(image)
    print("Imagen desencriptada y guardada como 'decrypted.jpg'.")

def main():
    while True:
        print("\n1. Encriptar Imagen")
        print("2. Desencriptar Imagen")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            encrypt_image()
        elif opcion == "2":
            decrypt_image()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
