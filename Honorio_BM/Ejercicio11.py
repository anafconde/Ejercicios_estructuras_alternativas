#Autor: Honorio
#Version: 1.0
#11.Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a=int(input("Introduzca el lado a: "))
b=int(input("Introduzca el lado b: "))
c=int(input("Introduzca el lado c: "))
pitagoras=(a**2 + b**2 == c**2)
if pitagoras:
    print("Es triangulo rectangulo")
elif a == b != c:
    print("Es isosceles")
elif a == b == c:
    print("Es equilatero")
else:
    print("Es escaleno")

