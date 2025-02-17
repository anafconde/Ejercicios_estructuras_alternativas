#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

#Pedir los datos necesario
base=float(input("Introduce la base: "))
exp=float(input("Introudce el exponente: "))

#Comprobar
if exp>0:
    print(f"La potencia de la base es {base**exp}")
if exp==0:
    print("La potencia es 1")
else:
    print(f"La potencia de la base es {abs(1/(base**exp))}")