#Lidia Castro Gutiérrez
#version 2

#Ejercicio1. Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

n1=int(input("Dime un número:"))
n2=int(input("Dime otro número:"))

if n1>n2:
    print(f"El numero {n1} es mayor que {n2}")
elif n1<n2:
    print(f"El numero {n1} es menor que {n2}")
else:
    print(f"El numero {n1} es igual que {n2}")