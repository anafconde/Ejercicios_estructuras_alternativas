#Author: Miguel Angel Garcia

#Version: 1.0
#Py Version : 3.11

#Descripcion: Este programa pide dos números y realiza la división de ambos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num2 != 0:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es: {division}")
else:
    print("Error: No se puede dividir por cero.")