#Autor: Honorio
#Version: 1.0
#7.Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.


base=int(input("Introduzca la base: "))
expon=int(input("Introduzca el exponente: "))
pont=(base**expon)
resul=(1/abs(pont))
if expon>0:
    print(f"El resultado es {pont}")
elif expon==0:
    print("El resultado es 1")
else:
    print(f"El resultado es {resul} {expon}")




