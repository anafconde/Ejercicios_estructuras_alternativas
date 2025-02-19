#Lidia Castro Gutiérrez
#version 2

#Ejercicio11. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A=float(input("Dime un lado del triángulo: "))
B=float(input("Dime otro lado del triángulo: "))
C=float(input("Dime otro lado del triángulo: "))

if (A**2+B**2)==(C**2):
     print(f"El triángulo cumple Pitágoras y es un triángulo rectángulo")
elif A==B!=C:
     print(f"El triángulo es isósceles")
elif A==B==C:
     print(f"El triángulo es equilátero")
else:
     print(f"El triángulo es escaleno")
