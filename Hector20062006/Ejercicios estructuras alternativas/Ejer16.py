# Ejercicio 16
minutos = int(input("Introduce la duración de la llamada en minutos: "))

# Cálculo del costo base
if minutos <= 5:
    costo_base = 1.0
else:
    costo_base = 1.0  # costo de los primeros 5 minutos
    if minutos <= 8:
        costo_base += (minutos - 5) * 0.80
    else:
        costo_base += 3 * 0.80  # minutos 6 a 8
        if minutos <= 10:
            costo_base += (minutos - 8) * 0.70
        else:
            costo_base += 2 * 0.70  # minutos 9 y 10
            costo_base += (minutos - 10) * 0.50

# Aplicación del impuesto
domingo = input("¿Es domingo? (S/N): ").upper()
if domingo == "S":
    impuesto = costo_base * 0.03
else:
    turno = input("¿Turno de la llamada? (M para mañana, T para tarde): ").upper()
    if turno == "M":
        impuesto = costo_base * 0.15
    elif turno == "T":
        impuesto = costo_base * 0.10
    else:
        impuesto = 0  # O bien, gestionar el error

total = costo_base + impuesto

print("Costo base:", costo_base, "euros")
print("Impuesto:", impuesto, "euros")
print("Total a pagar:", total, "euros")
