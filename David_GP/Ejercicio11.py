# Version 1.0
# Autor David García Pérez

#Ejercicio 11
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

# Pedir al usuario que ingrese las dimensiones de los lados del triángulo
a = float(input("Ingresa la longitud del lado A: "))
b = float(input("Ingresa la longitud del lado B: "))
c = float(input("Ingresa la longitud del lado C: "))

# Verificar si se cumple el teorema de Pitágoras
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("El triángulo es rectángulo")

# Verificar si es isósceles
elif a == b or a == c or b == c:
    print("El triángulo es isósceles")

# Verificar si es equilátero
elif a == b == c:
    print("El triángulo es equilátero")

# Si no se cumple ninguna de las condiciones anteriores, es escaleno
else:
    print("El triángulo es escaleno")