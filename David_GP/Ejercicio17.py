# Version 1.0
# Autor David García Pérez

#Ejercicio 17
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

def numero_a_letras(numero):
#Convierte un número a su equivalente en palabras
    numeros_en_letras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis"
    }
    return numeros_en_letras.get(numero, "ERROR: número incorrecto")

def cara_opuesta(cara):
#Devuelve la cara opuesta del dado según el número introducido
    if cara == 1:
        return 6
    elif cara == 2:
        return 5
    elif cara == 3:
        return 4
    elif cara == 4:
        return 3
    elif cara == 5:
        return 2
    elif cara == 6:
        return 1
    else:
        return None  # En caso de número fuera de rango

# Solicitar el resultado del dado
resultado = int(input("Introduce el número obtenido al lanzar el dado (1-6): "))

# Verificar si el número es válido y mostrar el resultado
cara_opuesta_resultado = cara_opuesta(resultado)

if cara_opuesta_resultado is None:
    print("ERROR: número incorrecto.")
else:
    # Mostrar la cara opuesta en números y en letras
    print(f"La cara opuesta al número {resultado} es {cara_opuesta_resultado} ({numero_a_letras(cara_opuesta_resultado)})")