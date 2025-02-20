#Autor: Juan Manuel López Torres
#Escribir un programa que lea un año e indique si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

año=int(input("Indique un año para comprobar si es bisiesto: "))

if año % 4 == 0:
    print("Es un año bisiesto!!!!")
elif año % 100 != 0:
    print("No es un año bisiesto")
elif año % 400 == 0:
    print("Es un año bisiesto")