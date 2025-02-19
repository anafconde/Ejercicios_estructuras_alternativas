#-----Autor:Israel---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no

n1=float(input("Introduce el primer número: "))
n2=float(input("Introduce el segundo número: "))

if n1>n2:
    print(f"El número {n1} es mayor")
elif n1==n2:
    print(f"Los números {n1} y {n2} son iguales")
else:
    print(f"El número {n2} es mayor")