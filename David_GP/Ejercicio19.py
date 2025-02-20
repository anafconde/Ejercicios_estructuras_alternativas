# Version 1.0
# Autor David García Pérez

#Ejercicio 19
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

def obtener_dias_del_mes(numero_mes):
    #Devuelve el número de días del mes correspondiente al número dado
    dias_mes = {
        1: 31,  #Enero
        2: 28,  #Febrero
        3: 31,  #Marzo
        4: 30,  #Abril
        5: 31,  #Mayo
        6: 30,  #Junio
        7: 31,  #Julio
        8: 31,  #Agosto
        9: 30,  #Septiembre
        10: 31, #Octubre
        11: 30, #Noviembre
        12: 31  #Diciembre
    }
    return dias_mes.get(numero_mes, "ERROR: número incorrecto")

# Solicitar el número del mes
numero_mes = int(input("Introduce un número de mes entre 1 y 12: "))

# Mostrar el número de días del mes correspondiente o error
print(obtener_dias_del_mes(numero_mes))