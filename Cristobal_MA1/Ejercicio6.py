# Author: Cris Moreno
# Version: 7.77
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

texto=(input("Dime una cadena de texto: "))

if texto == texto.upper():
    print("Tu cadena esta en mayusculas")
else:
    print("Tu cadena esta en minusculas")
