# Author: Cris Moreno
# Version: 7.77
    #Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1, r2 de dos
    #circunferencias y las clasifique en uno de estos estados:
    #- exteriores
    #- tangentes exteriores
    #- secantes
    #- tangentes interiores
    #- interiores
    #- concéntricas

import math

x1=float(input("Dime el eje x del primer circulo: "))
y1=float(input("Dime el eje y del primer circulo: "))
r1=float(input("Dime el radio del primer circulo: "))
x2=float(input("Dime el eje x del segundo circulo: "))
y2=float(input("Dime el eje y del segundo circulo: "))
r2=float(input("Dime el radio del segundo circulo: "))

d=math.sqrt((x2-x1)**2+(y2-y1)**2)

if d > (r1+r2):
    print("Son exteriores")
elif d==(r1+r2):
    print("Son tangentes exteriores")
elif (abs(r1-r2)) < d < (r1+r2):
    print("Son secantes")
elif d == (abs(r1-r2)):
    print("Son tangentes interiores")
elif d < (abs(r1-r2)):
    print("Son interiores")
else:
    print("Son concentricos")









