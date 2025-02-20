# Author: Luis Palacios
# Version: 1.0

# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error.

nsemana=int(input("Introduce el número del día de la semana: "))

if nsemana == 1:
    print("Hoy es lunes")
elif nsemana == 2:
    print("Hoy es martes")
elif nsemana == 3:
    print("Hoy es miercoles")
elif nsemana == 4:
    print("Hoy es jueves")
elif nsemana == 5:
    print("Hoy es viernes")
elif nsemana == 6:
    print("Hoy es sábado")
elif nsemana == 7:
    print("Hoy es domingo")
else:
    print("Error, válido un número del 1 al 7")