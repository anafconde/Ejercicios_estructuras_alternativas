#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
#La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje

n_alum=int(input("Introduzca el número de alumnos que asistirán al viaje de estudios: "))

if n_alum>=100:
    costo=65
    pago=costo*n_alum
    print(f"Para un viaje de {n_alum}, cada alumno deberá pagar un total de {pago} €")
elif n_alum>=50 and n_alum<=99:
    costo=70
    pago=costo*n_alum
    print(f"Para un viaje de {n_alum}, cada alumno deberá pagar un total de {pago} €")
elif n_alum>=30 and n_alum<=49:
    costo=95
    pago=costo*n_alum
    print(f"Para un viaje de {n_alum}, cada alumno deberá pagar un total de {pago} €")
elif n_alum>=0 and n_alum<=29:
    pago=4000/n_alum
    print(f"Para un viaje de {n_alum}, cada alumno deberá pagar un total de {pago} €")
else:
    print("Valor introducido erróneo")