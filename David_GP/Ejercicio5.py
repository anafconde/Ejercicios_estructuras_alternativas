# Version 1.0
# Autor David García Pérez

#Ejercicio 5
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario=input("Introduce tu nombre de usuario: ")
contraseña=input("Introduce tu contraseña: ")

if usuario=="pepe" and contraseña=="asdasd":
  print("Has entrado al sistema")
else:
  print("Error: nombre de usuario o contraseña incorrectos")