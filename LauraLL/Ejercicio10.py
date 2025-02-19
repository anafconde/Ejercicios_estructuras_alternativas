#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1, r2 de dos circunferencias y las clasifique en uno de estos estados:
#exteriores, tangentes exteriores, secantes, tangentes interiores, interiores, concéntricas

import math

print("Por favor, introduzca los valores del centro de la primera circunferencia: ")
x1=float(input("Valor de x1: "))
y1=float(input("Valor de y1: "))
r1=float(input("Valor del radio: "))

print("Por favor, introduzca los valores del centro de la segunda circunferencia: ")
x2=float(input("Valor de x2: "))
y2=float(input("Valor de y2: "))
r2=float(input("Valor del radio: "))

#Compruebo que el radio no es igual a 0 o negativo porque el radio no puede ser cero ni negativo ya que en ese caso no habría circunferencia
if (r1==0 or r2==0) or (r1<0 or r2<0):
    print("Error, alguno de los radios introducidos tiene valor 0 o negativo")
    exit()

#Calculo la distancia entre los dos puntos de las dos circunferencias
d=math.sqrt((x2-x1)**2)+((y2-y1)**2)


#Las circunferencias son exteriores si la distancia entre ellas es mayor que la suma de los radios de ambas (por eso están separadas)
if d > abs(r1+r2):
    print("Las circunferencias son EXTERIORES")

#Las circunferencias son tangentes exteriores si la distancia es igual a la suma de los radios (por eso se están tocando) 
elif d == abs(r1+r2):
    print("Las circunferencias son TANGENTES EXTERIORES")

#Las circunferencias son secantes cuando la distancia es menor que la suma de ambos radios (por eso están tocándose una con la otra en dos puntos)
#pero también tiene que ser mayor a la resta de ambos radios, porque sino ya sería interior, tanto tangente interior como interior o concéntrica
elif abs(r1-r2) < d < abs(r1+r2):
    print("Las circunferencias son SECANTES")

#Las circunferencias son tangentes interiores cuando la distancia es igual a la resta del radio de la circunferencia grandota menos la chiquita
elif d == abs(r1-r2) or d == abs(r2-r1):
    print("Las circunferencias son TANGENTES INTERIORES")

#Las circunferencias son interiores cuando la distancia es menor a la resta del radio de la circunferencia grandota menos la chiquita
#pero también mayor que 0 (porque sino serían concéntricas)
elif d < abs(r1-r2) and d>0:
    print("Las circunferencias son INTERIORES")

#Las circunferencias son concéntricas cuando ambos puntos centrales coinciden, por lo que la distancia es 0 (que es en este if, el resto de casos)
else:
    print("Las circunferencias son CONCÉNTRICAS")