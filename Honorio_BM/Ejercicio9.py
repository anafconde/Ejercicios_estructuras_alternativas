#Autor: Honorio
#Version: 1.0
#9.Algoritmo que pide tres números y los muestrean ordenados (de mayor a menor).
n1=int(input("Introduzca el primer numero: "))
n2=int(input("Introduzca el segundo numero: "))
n3=int(input("Introduzca el tercer numero: "))

if n1>=n2 and n1>=n3 and n2>=n3:
    print(f"{n1} > {n2} > {n3}")
else:
    print(f"{n1} < {n2} < {n3}")




