# Autor: Mohamed Mchachi
# Versión: 1.1
# Enunciado: Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.


Usuario = input("Ingresa tu nombre de usuario: ")
Contraseña = input("Ingresa tu contraseña: ")


if Usuario == "pepe" and Contraseña == "asdasd":
    print("Felicidades don pollo")
else:
    print("Error: Usuario o contraseña incorrectos")
