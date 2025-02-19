#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

mes = int(input("Introduce un número de mes (1-12): "))

if mes == 1:
    print("El mes 1 tiene 31 días.")
elif mes == 2:
    print("El mes 2 tiene 28 días.")
elif mes == 3:
    print("El mes 3 tiene 31 días.")
elif mes == 4:
    print("El mes 4 tiene 30 días.")
elif mes == 5:
    print("El mes 5 tiene 31 días.")
elif mes == 6:
    print("El mes 6 tiene 30 días.")
elif mes == 7:
    print("El mes 7 tiene 31 días.")
elif mes == 8:
    print("El mes 8 tiene 31 días.")
elif mes == 9:
    print("El mes 9 tiene 30 días.")
elif mes == 10:
    print("El mes 10 tiene 31 días.")
elif mes == 11:
    print("El mes 11 tiene 30 días.")
elif mes == 12:
    print("El mes 12 tiene 31 días.")
else:
    print("Número de mes no válido. Debe estar entre 1 y 12.")
