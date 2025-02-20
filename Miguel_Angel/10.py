#Author: Miguel Angel Garcia

#Version: 1.0
#Py Version : 3.11

#Descripcion: Programa que clasifica dos circunferencias en función de su posición relativa

x1 = float(input("Introduce el valor de x1: "))
y1 = float(input("Introduce el valor de y1: "))
r1 = float(input("Introduce el valor de r1: "))
x2 = float(input("Introduce el valor de x2: "))
y2 = float(input("Introduce el valor de y2: "))
r2 = float(input("Introduce el valor de r2: "))

distancia_cuadrada = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
r1_mas_r2_cuadrado = (r1 + r2) * (r1 + r2)
r1_menos_r2_cuadrado = (r1 - r2) * (r1 - r2)

if distancia_cuadrada > r1_mas_r2_cuadrado:
    print("Las circunferencias son exteriores")
elif distancia_cuadrada == r1_mas_r2_cuadrado:
    print("Las circunferencias son tangentes exteriores")
elif distancia_cuadrada < r1_mas_r2_cuadrado and distancia_cuadrada > r1_menos_r2_cuadrado:
    print("Las circunferencias son secantes")
elif distancia_cuadrada == r1_menos_r2_cuadrado and distancia_cuadrada != 0:
    print("Las circunferencias son tangentes interiores")
elif distancia_cuadrada < r1_menos_r2_cuadrado:
    print("Las circunferencias son interiores")
elif distancia_cuadrada == 0 and r1 == r2:
    print("Las circunferencias son concéntricas")
else:
    print("Las circunferencias no se pueden clasificar con los datos proporcionados")