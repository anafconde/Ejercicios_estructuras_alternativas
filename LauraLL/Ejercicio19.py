#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente

num=int(input("Escriba un número del 1 al 12 para saber cuántos días tiene ese mes: "))

if num<1 or num>12:
    print("ERROR: valor introducido no válido")
#Comprobamos los meses de 30 días porque son menos (abril, junio, septiembre y noviembre)
elif num==4 or num==6 or num==9 or num==11:
    print("El mes introducido tiene 30 días")
#Comprobamos febrero
elif num==2:
    print("El mes introducido tiene 28 días salvo en año bisiesto, que tiene 29")
#Comprobamos el resto de meses
else:
    print("El mes introducido tiene 31 días")