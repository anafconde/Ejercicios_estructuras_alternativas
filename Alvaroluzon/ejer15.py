alumnos = int(input("Introduce el número de alumnos: "))

if alumnos >= 100:
    costo = 65
    total = alumnos * costo
else:
    if alumnos >= 50:
        costo = 70
        total = alumnos * costo
    else:
        if alumnos >= 30:
            costo = 95
            total = alumnos * costo
        else:
            total = 4000
            costo = total / alumnos

print("El pago a la compañía es:", total, "euros.")
print("Cada uno debe pagar:", costo, "euros.")
