# Version 1.0
# Autor David García Pérez

#Ejercicio 3
#Escribe un programa que lea un número e indique si es par o impar.

numero=int(input("Dame un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")