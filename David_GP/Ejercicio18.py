# Version 1.0
# Autor David García Pérez

#Ejercicio 18
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

# Pedir al usuario que ingrese el día de la semana
dia_semana = int(input("Ingresa el día de la semana (1-7): "))

# Verificar si el número es válido
if dia_semana < 1 or dia_semana > 7:
    print("ERROR: Número incorrecto.")
else:
# Determinar el día de la semana
    if dia_semana == 1:
        dia = "Lunes"
    elif dia_semana == 2:
        dia = "Martes"
    elif dia_semana == 3:
        dia = "Miércoles"
    elif dia_semana == 4:
        dia = "Jueves"
    elif dia_semana == 5:
        dia = "Viernes"
    elif dia_semana == 6:
        dia = "Sábado"
    else:
        dia = "Domingo"

# Mostrar el día de la semana
    print(f"El día {dia_semana} de la semana es el {dia}")