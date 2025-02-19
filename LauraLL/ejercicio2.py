#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Algoritmo que pida un número y diga si es positivo, negativo o 0

n=int(input("Introduzca el número a comprobar: "))

if n<0:
    print(f"El número {n} es negativo")
elif n==0:
    print(f"El número {n} es 0")
else:
    print(f"El número {n} es positivo")