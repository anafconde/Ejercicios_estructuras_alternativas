# Version 1.0
# Autor David García Pérez

#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor):

# Pedir los tres números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Ordenar los números de mayor a menor
print("Los números ordenados de mayor a menor son:")

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1)
else:
    if numero1 >= numero2:
        print(numero3, numero1, numero2)
    else:
        print(numero3, numero2, numero1)