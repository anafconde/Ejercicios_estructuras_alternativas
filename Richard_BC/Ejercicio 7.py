#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
ano = int(input("Introduce el año: "))

if mes < 1 or mes > 12:
    print("Fecha incorrecta: mes no valido.")
elif dia < 1 or (mes == 2 and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (dia > 31):
    print("Fecha incorrecta: día no valido.")
elif ano < 1:
    print("Fecha incorrecta: año no valido.")
else:
    print("La fecha es correcta.")