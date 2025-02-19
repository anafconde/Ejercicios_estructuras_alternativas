#Lidia Castro Gutiérrez
#version 2

#Ejercicio13. Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Dime un dia (número): "))
mes = int(input("Dime un mes (número): "))
año = int(input("Dime un año: "))

if año < 1:
    print("Ese año no existe.")
elif mes < 1 or mes > 12:
    print("Ese mes no existe.")
elif dia < 1 or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
    print("Ese día no existe.")
elif dia < 1 or (mes in [4, 6, 9, 11] and dia > 30):
    print("Ese día no existe.")
elif dia < 1 or (mes == 2 and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and dia > 29):
    print("Ese día no existe.")
elif dia < 1 or (mes == 2 and not ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and dia > 28):
    print("Ese día no existe.")
else:
    print(f"El día {dia} del mes {mes} del año {año} es una fecha correcta.")





