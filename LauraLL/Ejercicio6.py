#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula

cadena=input("Por favor, introduzca una cadena de caracteres: ")

if cadena==cadena.upper():
    print(f"La cadena {cadena} está en mayúsculas")
else:
    print(f"La cadena {cadena} está en minúsculas")