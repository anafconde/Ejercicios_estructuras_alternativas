#Autor: Juan Manuel López Torres
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

dia_semana=int(input("Indique un dia de la semana, contando que 1 es Lunes y 7 es Domingo: "))

if dia_semana == 1:
    print("Has indicado Lunes")
elif dia_semana == 2:
    print("Has indicado Martes")
elif dia_semana == 3:
    print("Has indicado Miércoles")
elif dia_semana == 4:
    print("Has indicado Jueves")
elif dia_semana == 5:
    print("Has indicado Viernes")
elif dia_semana == 6:
    print("Has indicado Sábado")
elif dia_semana == 7:
    print("Has indicado Domingo")
else:
    print("Error. Opción inválida...")