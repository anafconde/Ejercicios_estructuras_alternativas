#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.


# #version 1.0
#author Senén Lara


numero_dia = int(input("Introduce un número del 1 al 7: "))

if numero_dia == 1:
    dia_semana = "Lunes"
elif numero_dia == 2:
    dia_semana = "Martes"
elif numero_dia == 3:
    dia_semana = "Miércoles"
elif numero_dia == 4:
    dia_semana = "Jueves"
elif numero_dia == 5:
    dia_semana = "Viernes"
elif numero_dia == 6:
    dia_semana = "Sábado"
elif numero_dia == 7:
    dia_semana = "Domingo"
else:
    print("Error, introduce bien el dia de la semana")
    
print("Tu dia es:", dia_semana, "Disfruta")

