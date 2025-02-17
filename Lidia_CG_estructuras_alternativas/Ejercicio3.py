#Lidia Castro Gutiérrez
#version 2

#Ejercicio3.Escribe un programa que lea un número e indique si es par o impar.

n=int(input("Dime un número:"))

if n%2==0:
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")