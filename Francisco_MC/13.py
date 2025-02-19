#Version
#Enunciado del algoritmo Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes == 2:
    if dia >= 1 and dia <= 29:
        print("La fecha es correcta.")
    else:
        print("La fecha no es correcta.")
elif mes in [4, 6, 9, 11]:
    if dia >= 1 and dia <= 30:
        print("La fecha es correcta.")
    else:
        print("La fecha no es correcta.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia >= 1 and dia <= 31:
        print("La fecha es correcta.")
    else:
        print("La fecha no es correcta.")
else:
    print("La fecha no es correcta.")