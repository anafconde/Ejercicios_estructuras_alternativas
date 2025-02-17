# Author: Cris Moreno
# Version: 7.77
#Algoritmo que pida un número y diga si es positivo, negativo o 0.

num=int(input("Dime un numero: "))
if num==0:
    print("Tu numero es 0")
elif num<0:
    print("Tu numero es negativo")
else:
    print("Tu numero es positivo")