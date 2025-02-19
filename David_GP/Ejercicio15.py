# Version 1.0
# Autor David García Pérez

#Ejercicio 15
#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

# Determinar el costo por alumno y el costo total a la compañía
def calcular_pago(alumnos):
    if alumnos >= 100:
        costo_alumno = 65
        costo_total = alumnos * costo_alumno
    elif 50 <= alumnos <= 99:
        costo_alumno = 70
        costo_total = alumnos * costo_alumno
    elif 30 <= alumnos <= 49:
        costo_alumno = 95
        costo_total = alumnos * costo_alumno
    else:
        costo_alumno = 4000 / alumnos  # Costo fijo de 4000 euros para menos de 30 alumnos
        costo_total = 4000  # La renta del autobús es 4000 euros

    return costo_total, costo_alumno

# Solicitar al usuario el número de alumnos
alumnos = int(input("Ingrese el número de alumnos: "))

# Calcular el pago y mostrar el resultado
pago_total, pago_alumno = calcular_pago(alumnos)
print(f"El total a pagar a la compañía de autobuses es: {pago_total} €")
print(f"El costo por alumno es: {pago_alumno} €")