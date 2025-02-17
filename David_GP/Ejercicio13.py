# Version 1.0
# Autor David García Pérez

#Ejercicio 13
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

def fecha_valida(dia, mes, año):

  if año < 1 or mes < 1 or mes > 12 or dia < 1:
    return False
  dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    dias_en_mes[1] = 29
  return dia <= dias_en_mes[mes - 1]

# Solicitar la fecha al usuario
dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
año = int(input("Ingresa el año: "))

# Verificar si la fecha es válida
if fecha_valida(dia, mes, año):
  print("La fecha es válida.")
else:
  print("La fecha no es válida.")
