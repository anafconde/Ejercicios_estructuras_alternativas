# Version 1.0
# Autor David García Pérez

#Ejercicio 16
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

# Pedir al usuario que ingrese los datos de la llamada
dia_semana = input("Ingresa el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ")
turno = input("Ingresa el turno (Mañana, Tarde): ")
duracion = int(input("Ingresa la duración de la llamada en minutos: "))

# Calcular el costo de la llamada
costo_total = 0

if duracion <= 5:
    costo_total += 1
elif duracion <= 8:
    costo_total += 1 + (duracion - 5) * 0.8
elif duracion <= 10:
    costo_total += 1 + 3 * 0.8 + (duracion - 8) * 0.7
else:
    costo_total += 1 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5

# Calcular el impuesto
if dia_semana == "Domingo":
    impuesto = costo_total * 0.03
elif turno == "Mañana":
    impuesto = costo_total * 0.15
elif turno == "Tarde":
    impuesto = costo_total * 0.10
else:
    impuesto = 0

# Mostrar el costo de la llamada y el impuesto
print(f"Costo de la llamada: {costo_total} euros")
print(f"Impuesto: {impuesto} euros")

# Mostrar el costo total
print(f"Costo total: {costo_total + impuesto} euros")