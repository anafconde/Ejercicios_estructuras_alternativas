# Version 1.0
# Autor David García Pérez

#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor):

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)
print("Los números ordenados de mayor a menor son:", numeros)