#Lidia Castro Gutiérrez
#Versión 1

#Ejercicio5.Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario=input("Dime un usuario:")
pswd=input("Dime la contraseña: ")

if usuario=="pepe" and pswd=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error")
