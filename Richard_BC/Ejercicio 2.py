#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que lea un número e indique si es par o impar.

numero = int(input("Escribe el numero para saber si es par o impar: "))

if numero % 2 == 0:
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")
