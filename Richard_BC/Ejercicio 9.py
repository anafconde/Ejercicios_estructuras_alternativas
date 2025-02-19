#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

resultado = int(input("Introduce el resultado del dado (número del 1 al 6): "))


if resultado == 1:
    print(f"La cara opuesta al {resultado} es: Cinco")
elif resultado == 2:
    print(f"La cara opuesta al {resultado} es: Cuatro")
elif resultado == 3:
    print(f"La cara opuesta al {resultado} es: Tres")
elif resultado == 4:
    print(f"La cara opuesta al {resultado} es: Dos")
elif resultado == 5:
    print(f"La cara opuesta al {resultado} es: Uno")
elif resultado == 6:
    print(f"La cara opuesta al {resultado} es: Seis")
else:
    print("ERROR: numero incorrecto")