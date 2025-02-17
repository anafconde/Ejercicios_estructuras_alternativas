def es_mayuscula(cadena):
    if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
        return True
    return False

cadena = input("Introduce una cadena: ")
if es_mayuscula(cadena):
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")