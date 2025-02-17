#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

#Pedimos los dos números necesarios
n1=float(input("Introduce el primer número: "))
n2=float(input("Introduce el segundo número: "))

#Comprobación
if n1==n2:
    print("Los números son iguales")
elif n1>n2:
    print(f"El número {n1} es MAYOR que el número {n2}")
else:
    print(f"El número {n2} es MAYOR que el número {n1}")
