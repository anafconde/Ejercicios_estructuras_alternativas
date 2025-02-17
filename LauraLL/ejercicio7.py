#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

print("Para realizar la potencia, introduzca...")
base=int(input("La base: "))
exponente=int(input("El exponente: "))

potencia=base**exponente
potencia2=1/(base**abs(exponente))

if exponente>0:
    print(f"La potencia de la base {base} elevado a {exponente} es {potencia}")
elif exponente==0:
    print(f"La potencia de la base {base} elevado a {exponente} es 1")
else:
    print(f"La potencia de la base {base} elevado a {exponente} es {potencia2}")