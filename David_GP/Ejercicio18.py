# Version 1.0
# Autor David García Pérez

#Ejercicio 18
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

def obtener_dia(numero):
# Devuelve el nombre del día correspondiente al número ingresado.
    dias_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}
    return dias_semana.get(numero, "ERROR: número incorrecto")

# Solicitar el día de la semana
numero = int(input("Introduce el número del día de la semana (1-7): "))

# Mostrar el día correspondiente o error
print(obtener_dia(numero))
