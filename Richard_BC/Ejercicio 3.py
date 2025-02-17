#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario= "pepe"
contrasena = "asdasd"

usuarioP = input("Introduce tu nombre de usuario: ")
contrasenaP = input("Introduce tu contraseña: ")

if usuarioP == usuario and contrasenaP == contrasena:
    print("Has entrado al sistema")
else:
    print("Error: Usuario o contraseña incorrectos")
