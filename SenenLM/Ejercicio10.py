#version 1.0
#author Senén Lara
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
r1 = float(input("Introduce r1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
r2 = float(input("Introduce r2: "))



distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Clasificación de las circunferencias
if distancia_centros > r1 + r2:
        print("Exteriores")
elif distancia_centros == r1 + r2:
        print( "Tangentes Exteriores")
elif distancia_centros < r1 + r2 and distancia_centros > abs(r1 - r2):
        print( "Secantes")
elif distancia_centros == abs(r1 - r2):
        print( "Tangentes Interiores" )
elif distancia_centros < abs(r1 - r2):
        print( "Interiores" )
elif distancia_centros == 0 and r1 == r2:
        print( "Concéntricas" )
else:
        print( "No clasificado" )


