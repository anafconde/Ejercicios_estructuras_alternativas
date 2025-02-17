#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Escribe un programa que lea un número e indique si es par o impar.

#Pedir un número
n=float(input("Introduce un número: "))

#Comprobar con el resto dividiendo entre dos
resto=n%2

if resto==0:
    print(f"El número {n} es PAR")
else:
    print(f"El número {n} es IMPAR")
