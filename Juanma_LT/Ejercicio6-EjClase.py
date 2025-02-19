#Autor: Juan Manuel López Torres
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena=input("Introduzca una cadena de caracteres: ")

if cadena == cadena.upper():
    print("La cadena tiene letra mayúscula")
else:
    print("La cadena de caracteres no contiene ninguna mayúscula")