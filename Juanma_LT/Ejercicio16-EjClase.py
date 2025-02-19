#Autor: Juan Manuel López Torres
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.ç

# Solicitar datos al usuario
duracion = float(input("Ingrese la duración de la llamada en minutos: "))
dia = input("Ingrese el día de la semana (ejemplo: lunes, martes, domingo): ")
turno = input("Ingrese el turno (mañana o tarde): ")

# Definición de tarifas
costo = 0

# Cálculo del costo según la duración de la llamada
if duracion <= 5:
    costo = 1
elif duracion <= 8:
    costo = 1 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo = 1 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo = 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

# Cálculo del impuesto
if dia.lower() == 'domingo':
    impuesto = 0.03  
else:
    if turno.lower() == 'mañana':
        impuesto = 0.15  
    else:
        impuesto = 0.10  

# Cálculo del costo total
costo_total = costo + (costo * impuesto)

# Mostrar resultados
print(f"Costo de la llamada: {costo} euros")
print(f"Impuesto aplicado: {impuesto * 100}%")
print(f"Costo total a pagar: {costo_total} euros")