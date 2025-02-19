#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario

n1=int(input("Introduzca el número a dividir: "))
n2=int(input("Introduzca el número por el que lo quiere dividir: "))

if n2!=0:
    div=n1/n2
    print(f"El resultado de la división de {n1} entre {n2} es: {div}")
else:
    print("Error, no se puede hacer la división porque el segundo número introducido es 0")