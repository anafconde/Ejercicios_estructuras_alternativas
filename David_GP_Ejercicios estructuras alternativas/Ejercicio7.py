# Version="1.0"
# Autor David García Pérez

#Ejercicio 7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Introduce una base: "))
exponente = int(input("Introduce un exponente: "))

if exponente < 0:
    print(1 / (base ** abs(exponente)))
elif exponente == 0:
    print(1)
else:
    print(base ** exponente)