#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

#Pedir los números
n1=float(input("Introduce el primer dígito: "))
n2=float(input("Introduce el segundo dígito: "))
n3=float(input("Introduce el tercer dígito: "))

#Comprobación
if n1==n2 and n2==n3:
    print("Los números introducidos son iguales")
elif n1>n2 and n1>n3: #SI N1 es el MAYOR
    if n2>n3:
        print(f"{n1} > {n2} > {n3}")
    elif n2==n3:
        print(f"{n1} > {n2 } = {n3}")
    else:
        print(f"{n1} > {n3} > {n2}")
elif n2>n1 and n2>n3: #SI N2 es el MAYOR
    if n1>n3:
        print(f"{n2} > {n1} > {n3}")
    elif n1==n3:
        print(f"{n2} > {n1} = {n3}")
    else:
        print(f"{n2} > {n3} > {n1}")
elif n3>n1 and n3>n2: #SI N3 es el MAYOR
    if n1>n2:
        print(f"{n3} > {n1} > {n2}")
    elif n1==n2:
        print(f"{n3} > {n2} = {n1}")
    else:
        print(f"{n3} > {n2} > {n1}")
