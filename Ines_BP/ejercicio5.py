#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.


#Pedir usuario y contraseña
usu=input("Introduce el usuario: ")
pas=input("Introduce la contraseña: ")

if usu=="pepe" and pas=="asdasd":
    print("Has entrado al sistema")
else:
    print("ERROR")
