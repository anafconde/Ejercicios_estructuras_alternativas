#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Escribir un programa que lea un año e indique si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400

anyo=int(input("Introduzca el año a comprobar: "))

if ((anyo%4)==0 and (anyo%100)!=0) or (anyo%400)==0:
    print(f"El año {anyo} es bisiesto")
else:
    print(f"El año {anyo} no es bisiesto")