#Lidia Castro Gutiérrez
#version 2

#Ejercicio15. El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

n=int(input("Dime el número de alumnos que van al viaje: "))

if n>100:
    coste_bus=n*65
    coste=65
    print(f"El coste del viaje por alumno es de {coste} € y el pago a la compañía es de {coste_bus} €")
elif 50 <= n <= 99:
    coste_bus=n*70
    coste=70
    print(f"El coste del viaje por alumno es de {coste} € y el pago a la compañía es de {coste_bus} €")
elif 30 <= n <= 49:
    coste_bus=n*95
    coste=95
    print(f"El coste del viaje por alumno es de {coste} € y el pago a la compañía es de {coste_bus} €")
else:
    coste=4000/n
    print(f"El coste del viaje por alumno es de {coste} € y el pago a la compañía es de 4000€")
