#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Escribe un programa que pida un nombre de usuario y una contraseña y 
#si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error

nombre=input("Introduce el nombre de usuario: ")
passwd=input("Introduce la contraseña: ")

if nombre=="pepe" and passwd=="asdasd":
    print("Ha entrado en el sistema")
else:
    print("Error")