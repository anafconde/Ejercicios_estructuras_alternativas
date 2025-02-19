#version 1.0
#author Senén Lara

#Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
n1=int(input("Introduce tu numero: "))

if n1%4 == 0:
    if n1%100 != 0:
        print("Tu año es bisiesto")
    elif n1%100 == 0:
        if n1%400 == 0:
            print("Tu año es bisiesto")
        else:
            print("Tu año no es bisiesto")
    else:
        print("Tu año no es bisiesto")
else:
        print("Tu año no es bisiesto")