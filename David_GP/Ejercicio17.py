# Version 1.0
# Autor David García Pérez

#Ejercicio 17
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

# Pedir al usuario que ingrese el resultado del dado
numero_dado = int(input("Ingresa el número del dado (1-6): "))

# Verificar si el número es válido
if numero_dado < 1 or numero_dado > 6:
    print("ERROR: número incorrecto.")
else:
# Determinar la cara opuesta
    if numero_dado == 1:
        cara_opuesta = "6"
    elif numero_dado == 2:
        cara_opuesta = "5"
    elif numero_dado == 3:
        cara_opuesta = "4"
    elif numero_dado == 4:
        cara_opuesta = "3"
    elif numero_dado == 5:
        cara_opuesta = "2"
    elif numero_dado == 6:
        cara_opuesta = "1"
    else:
        print("ERROR: número incorrecto.")

# Mostrar la cara opuesta en letras
    print(f"La cara opuesta al {numero_dado} es: {cara_opuesta}")