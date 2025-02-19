#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada 
# alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 
# alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de
#  95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de 
# alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada 
# alumno por el viaje.

#Pedir el número de alumnos
nalum=int(input("Introduce el número de alumnos: "))

if nalum>=100: #SI EL NUMERO DE ALUMNOS ES MAYOR QUE 100
    costo=nalum*65
    print(f"El coste por alumnos es 65€ y el precio del autobues es {costo}€")
elif nalum>=50 and nalum<=99: #SI EL NUMERO DE ALUMNOS ES MAYOR IGUAL QUE 50 Y MENOS QUE 100
    costo=nalum*70
    print(f"El coste por alumnos es 70€ y el precio del autobues es {costo}€")
elif nalum>=30 and nalum<=49: #SI EL NUMERO DE ALUMNOS ES MAYOR IGUAL QUE 30 Y MENOS QUE 50
    costo=nalum*95
    print(f"El coste por alumnos es 95€ y el precio del autobues es {costo}€")
else: #SI EL NUMERO DE ALUMNOS ES MENOS QUE 30
    print(f"El coste por alumnos es {4000/nalum}€ y el precio del autobus es 4000€")
