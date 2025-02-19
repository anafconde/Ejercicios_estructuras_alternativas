#Lidia Castro Gutiérrez
#version 2

#Ejercicio19. Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

mes=int(input("Dime un mes (número entre 1 y 12): "))

if mes<1 or mes > 12:
    print("Ese mes no existe.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    print(f"El mes {mes} tiene 31 dias.")
elif mes in [4,6,9,11]:
    print(f"El mes {mes} tiene 30 dias.")
elif mes==2:
     print(f"El mes {mes} tiene 28 dias. O 29 dias si es bisiesto.")
