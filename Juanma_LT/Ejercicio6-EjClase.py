#Autor: Juan Manuel López Torres
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena=print(input("Introduzca una cadena de caracteres: "))

if cadena.isupper():
    print(f"La cadena tiene letra mayúscula")
else:
    print(f"La cadena de caracteres no contiene ninguna mayúscula")