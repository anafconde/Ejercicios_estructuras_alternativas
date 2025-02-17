# Autor: Mohamed Mchachi
# Versión: 1.1
# Enunciado: Algoritmo que pide dos números e indica si el primero es mayor, menor o igual al segundo.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El primer número es mayor que el segundo número.")
elif numero1 < numero2:
    print("El segundo número es mayor que el primer número.")
else:
    print("Los números son iguales.")
