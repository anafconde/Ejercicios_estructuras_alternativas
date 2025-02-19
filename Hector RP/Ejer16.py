
minutos = int(input("Introduce la duración de la llamada en minutos: "))


if minutos <= 5:
    costo_base = 1.0
else:
    costo_base = 1.0 
    if minutos <= 8:
        costo_base += (minutos - 5) * 0.80
    else:
        costo_base += 3 * 0.80
        if minutos <= 10:
            costo_base += (minutos - 8) * 0.70
        else:
            costo_base += 2 * 0.70
            costo_base += (minutos - 10) * 0.50


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
        impuesto = 0

total = costo_base + impuesto

print("Costo base:", costo_base, "euros")
print("Impuesto:", impuesto, "euros")
print("Total a pagar:", total, "euros")
