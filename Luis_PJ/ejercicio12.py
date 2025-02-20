# Autor: Luis Palacios
# Version: 1.0

# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

fecha=int(input("Introduce un año para saber si es bisiesto o no: "))

bisiesto=fecha%4
bisiesto2=fecha%100
bisiesto3=fecha%400

if bisiesto == 0 and bisiesto2 != 0:
    print("El año",fecha,"es bisiesto")
elif bisiesto3 == 0:
        print("El año",fecha,"es bisiesto")
else:
      print ("El año",fecha,"no es bisiesto")
    
