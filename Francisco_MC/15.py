#Version
#Enunciado del algoritmo El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Introduce el número de alumnos: "))

if alumnos >= 100:
    costo = 65
elif 50 <= alumnos <= 99:
    costo = 70
elif 30 <= alumnos <= 49:
    costo = 95
else:
    costo = 4000

pago_total = alumnos * costo
print(f"El pago a la compañía es: {pago_total} euros.")
print(f"El costo por alumno es: {costo} euros.")