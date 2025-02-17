#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

# Ordenar usando condicionales
if num1 >= num2 >= num3:
    ordenados = (num1, num2, num3)
elif num1 >= num3 >= num2:
    ordenados = (num1, num3, num2)
elif num2 >= num1 >= num3:
    ordenados = (num2, num1, num3)
elif num2 >= num3 >= num1:
    ordenados = (num2, num3, num1)
elif num3 >= num1 >= num2:
    ordenados = (num3, num1, num2)
else:
    ordenados = (num3, num2, num1)

print(f"Los numeros ordenados de mayor a menor es {ordenados}")