#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

n1=float(input("Introduzca el primer número: "))
n2=float(input("Introduzca el segundo número: "))
n3=float(input("Introduzca el tercer número: "))

if n1>n2 and n1>n3:
    if n2>n3:
        print(f"Los números ordenados son: {n1} > {n2} > {n3}")
    elif n3>n2:
        print(f"Los números ordenados son: {n1} > {n3} > {n2}")
    else:
        print(f"Los números ordenados son: {n1} > {n2} = {n3}")
elif n2>n1 and n2>n3:
    if n1>n3:
        print(f"Los números ordenados son: {n2} > {n1} > {n3}")
    elif n3>n1:
        print(f"Los números ordenados son: {n2} > {n3} > {n1}")
    else:
        print(f"Los números ordenados son: {n2} > {n1} = {n3}") 
elif n3>n1 and n3>n2:
    if n1>n2:
        print(f"Los números ordenados son: {n3} > {n1} > {n2}")
    elif n2>n1:
        print(f"Los números ordenados son: {n3} > {n2} > {n1}")
    else:
        print(f"Los números ordenados son: {n3} > {n1} = {n2}")
else:
    print(f"Todos los números son iguales {n1} = {n2} = {n3}")