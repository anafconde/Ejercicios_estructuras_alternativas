#Lidia Castro Gutiérrez
#version 2

#Ejercicio17. Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#Ejemplo:

#Introduzca número del dado: 5
#En la cara opuesta está el "dos".

n=int(input("Introduzca número del dado:"))

if n==1:
    print("En la cara opuesta está el \"seis\"")
elif n==2:
    print("En la cara opuesta está el \"cinco\"")
elif n==3:
    print("En la cara opuesta está el \"cuatro\"")
elif n==4:
    print("En la cara opuesta está el \"tres\"")
elif n==5:
    print("En la cara opuesta está el \"dos\"")
elif n==6:
    print("En la cara opuesta está el \"uno\"")
else:
    print("ERROR: número incorrecto.")