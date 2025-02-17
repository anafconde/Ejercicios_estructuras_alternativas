# Author: Luis Palacios
# Version: 1.0

#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena=input("Introduce una cadena de texto: ")

if cadena==cadena.upper():
    print("La cadena está en mayúscula")
else:
    print("Error, la cadena no está en mayúscula")