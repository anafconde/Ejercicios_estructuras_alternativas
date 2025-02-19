#Autor: Juan Manuel López Torres
#Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1, r2 de dos circunferencias y las clasifique en uno de estos estados:
#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas
import math

#En este paso se solicita los puntos centrales y los radios
x1=float(input("Incluye la coordenada x1 de la propia circunferencia: "))
y1=float(input("Incluye la coordenada y1 de la propia circunferencia: "))
r1=float(input("Incluye el radio de la primera circunferencia: "))

x2=float(input("Incluye la coordenada x2 de la propia circunferencia: "))
y2=float(input("Incluye la coordenada y2 de la propia circunferencia: "))
r2=float(input("Incluye el radio de la segunda circunferencia: "))


#En este paso vamos a calcular la distancia entre los centros
distancia=math.sqrt((x2-x1) **2 + (y2-y1) **2)

#El último paso trata de clasificar la relación de las circunferencias
if distancia > r1 + r2:
   print("Es una exterior")
elif distancia == r1 + r2:
    print("Tangentes exteriores")
elif r1 - r2 < distancia < r1 + r2:
    print("Secantes")
elif distancia == abs(r1 - r2):
    print("Tangentes interiores")
elif distancia < abs(r1 - r2):
    print("Interiores")
elif distancia == 0 and r1 == r2:
    print("Concentricas")