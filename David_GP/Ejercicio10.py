# Version 1.0
# Autor David García Pérez

#Ejercicio 10
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

import math

# Pedir al usuario que ingrese los datos de las circunferencias
x1 = float(input("Introduce la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Introduce la coordenada y del centro de la primera circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))
x2 = float(input("Introduce la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Introduce la coordenada y del centro de la segunda circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))

# Calcular la distancia entre los centros de las circunferencias
distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Clasificar la posición de las circunferencias
if distancia_centros > r1 + r2:
    print("Las circunferencias son exteriores.")
elif distancia_centros == r1 + r2:
    print("Las circunferencias son tangentes exteriores.")
elif distancia_centros > abs(r1 - r2) and distancia_centros < r1 + r2:
    print("Las circunferencias son secantes.")
elif distancia_centros == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")
elif distancia_centros < abs(r1 - r2):
    print("Las circunferencias son interiores.")
else:
    print("Las circunferencias son concéntricas.")