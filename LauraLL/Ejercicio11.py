#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
#El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A=float(input("Introduce el dato A de uno de los lados: "))
B=float(input("Introduce el dato B de uno de los lados: "))
C=float(input("Introduce el dato C de uno de los lados: "))

#Compruebo el teorema de Pitágoras
if C**2==((B**2)+(A**2)) or B**2==((A**2)+(C**2)) or A**2==((B**2)+(C**2)):
    print("Se cumple el teorema de Pitágoras, así que es un TRIÁNGULO RECTÁNGULO")
#Compruebo que todos los lados sean iguales
elif C==A and A==B:
    print("Es un TRIÁNGULO EQUILÁTERO")
#Compruebo que dos lados sean iguales pero que el otro sea distinto, da igual el lado
elif B==A or A==C or B==C:
    # if A!=C or A!=B or B!=C:
        print("Es un TRIÁNGULO ISÓSCELES")
#Ni no se cumple ninguna de las anteriores...
else:
    print("Es un TRIÁNGULO ESCALENO")