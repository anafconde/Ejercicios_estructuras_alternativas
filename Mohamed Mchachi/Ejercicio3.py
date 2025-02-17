# Autor: Mohamed Mchachi
# Versión: 1.1
# Enunciado: Escribe un programa que lea un número e indique si es par o impar.


numero = int(input("Ingrese un número: "))


if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
