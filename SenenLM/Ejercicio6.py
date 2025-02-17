#version 1.0
#author Senén Lara

#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.


cadena=input("Introduce la cadena de caracteres: ")
if cadena == cadena.upper():
    print("Esta en mayusculas")
else:
    print("Esta en minusculas")   
    
