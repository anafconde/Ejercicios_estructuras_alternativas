#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.


#Lectura de los 3 lados
a=float(input("Introduce el lado A: "))
b=float(input("Introduce el lado B: "))
c=float(input("Introduce el lado C: "))

if c**2==((a**2)+(b**2)):
    print("El triangulo introducido es un TRIANGULO RECTANGULO")
elif a==b and b==c:
    print("El triangulo es un TRIANGULO EQUILATERO")
elif a==b:
    if a!=c:
        print("El triangulo introducido es un TRIANGULO ISOSCELES")
elif c==b:
    if c!=a:
        print("El triangulo introducido es un TRIANGULO ISOSCELES")
elif a==c:
    if a!=b:
        print("El triangulo introducido es un TRIANGULO ISOSCELES")
else:
    print("El triangulo es un TRIANGULO ESCALENO")