# -*- coding: utf-8 -*-
import random
import string

def generar_password(longitud=16):
    caracteres = (
        string.ascii_letters +
        string.digits +

        string.punctuation
    )

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password


if __name__ == "__main__":
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))

        if longitud <= 0:
            print("La longitud debe ser mayor que 0.")
        else:
            print("\nContraseña generada:")
            print(generar_password(longitud))

    except ValueError:
        print("Debes introducir un número válido.")

