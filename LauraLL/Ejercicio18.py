#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error

n=int(input("Introduzca el número del día de la semana (1-7): "))

if n<1 and n>7:
    print(f"Error, el número {n} introducido no es válido")
else:
    if n==1:
        print("El día es LUNES")
    elif n==2:
        print("El día es MARTES")
    elif n==3:
        print("El día es MIÉRCOLES")
    elif n==4:
        print("El día es JUEVES")
    elif n==5:
        print("El día es VIERNES")
    elif n==6:
        print("El día es SÁBADO")
    else:
        print("El día es DOMINGO")