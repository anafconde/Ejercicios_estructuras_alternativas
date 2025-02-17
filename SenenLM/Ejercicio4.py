#version 1.0
#author Senén Lara

#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, 
#o un mensaje de aviso en caso contrario.


numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))
if numero2 == 0:
    print("No se puede hacer la division, error")
else:
    division=numero1/numero2
    print("La division es:", division)