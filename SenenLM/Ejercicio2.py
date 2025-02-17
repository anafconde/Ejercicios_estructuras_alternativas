#version 1.0
#author Senén Lara

#Algoritmo que pida un número y diga si es positivo, negativo o 0.

numero=int(input("Introduce el numero que queremos comprobar: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("El numero es 0")