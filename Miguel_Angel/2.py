#Author: Miguel Angel Garcia

#Version: 1.0
#Py Version : 3.11

#Descripcion: Este programa pide un número y verifica si es positivo, negativo o cero.

num = int(input("Introduce un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")