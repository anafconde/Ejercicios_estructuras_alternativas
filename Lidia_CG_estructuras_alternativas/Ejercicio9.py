#Lidia Castro Gutiérrez
#version 2

#Ejercicio9. Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

n1=int(input("Dime un número:"))
n2=int(input("Dime un segundo número:"))
n3=int(input("Dime un tercer número:"))

if n1>=n2 and n1>=n3 and n2>=n3:
    print(f"El orden de los números de mayor a menor es: {n1} {n2} {n3}")
elif n1>=n2 and n1>=n3 and n2<=n3:
    print(f"El orden de los números de mayor a menor es: {n1} {n3} {n2}")

elif n2>=n1 and n2>=n3 and n1>=n3:
    print(f"El orden de los números de mayor a menor es: {n2} {n1} {n3}")
elif n2>=n1 and n2>=n3 and n1<=n3:
    print(f"El orden de los números de mayor a menor es: {n2} {n3} {n1}")

elif n3>=n1 and n3>=n2 and n1>=n2:
    print(f"El orden de los números de mayor a menor es: {n3} {n1} {n2}")
elif n3>=n1 and n3>=n2 and n1<=n2:
    print(f"El orden de los números de mayor a menor es: {n3} {n2} {n1}")

