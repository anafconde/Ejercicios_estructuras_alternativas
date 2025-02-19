#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por
#pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

dado=int(input("¿Cuál ha sido el resultado de su dado de seis caras? "))

if dado>6 or dado<1:
    print("ERROR: número incorrecto")
else:
    if dado==1:
        print("La cara opuesta de su dado es SEIS")
    elif dado==2:
        print("La cara opuesta de su dado es CINCO")
    elif dado==3:
        print("La cara opuesta de su dado es CUATRO")
    elif dado==4:
        print("La cara opuesta de su dado es TRES")
    elif dado==5:
        print("La cara opuesta de su dado es DOS")
    else:
        print("La cara opuesta de su dado es UNO")