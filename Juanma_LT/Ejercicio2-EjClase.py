#Autor: Juan Manuel López Torres
#Algoritmo que pida un número y diga si es positivo, negativo o 0.

numero=int(input("Indique un número: "))

if numero > 0:
    print("El número es positivo...")
elif numero == 0:
    print("El numero es 0...")
else:
    print ("El número es negativo...")