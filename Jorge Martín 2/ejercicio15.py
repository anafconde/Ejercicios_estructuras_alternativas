def calcular_costo_viaje(num_alumnos):
    if num_alumnos >= 100:
        costo_por_alumno = 65
    elif 50 <= num_alumnos <= 99:
        costo_por_alumno = 70
    elif 30 <= num_alumnos <= 49:
        costo_por_alumno = 95
    else:
        return f"El costo total del autobús es de 4000 euros y cada alumno paga {4000 / num_alumnos:.2f} euros."

    total_pago = costo_por_alumno * num_alumnos
    return f"Cada alumno paga {costo_por_alumno} euros, total a pagar: {total_pago} euros."

num_alumnos = int(input("Ingrese el número de alumnos: "))
print(calcular_costo_viaje(num_alumnos))
