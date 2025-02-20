# Author: Cris Moreno
# Version: 7.77
## Ejercicio 12 📅
#Escribir un programa que lea un año e indique si es bisiesto. Nota: un año es bisiesto
#si es un número divisible por 4, pero no si es divisible por 100, excepto que también 
#sea divisible por 400.

anyo=int(input("Dime un año, te diré si es, fué o será bisiesto: "))

if anyo%4==0 and anyo%100!=0:
    print("El año es bisiesto")
elif anyo%4==0 and anyo%100==0 and anyo%400==0:  
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

