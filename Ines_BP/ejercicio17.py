#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al 
#lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena)
#de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#  “ERROR: número incorrecto.”.

#Leer el dato
cara=int(input("Introduce el número obtenido: "))

if cara<1 and cara>6:  #Comprobar la condicion erronea
    print("ERROR: número incorrecto.")
else:
    if cara==1:print("La cara contraria es: SEIS")
    elif cara==2:print("La cara contraria es: CINCO")
    elif cara==3:print("La cara contraria es: CUATRO")
    elif cara==4:print("La cara contraria es: TRES")
    elif cara==5:print("La cara contraria es: DOS")
    elif cara==6:print("La cara contraria es: UNO")