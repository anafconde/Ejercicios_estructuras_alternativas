# Ejercicio 10
import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
r1 = float(input("Introduce el radio r1: "))
r2 = float(input("Introduce el radio r2: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if x1 == x2 and y1 == y2:
    print("Las circunferencias son concéntricas.")
else:
    if d > (r1 + r2):
        print("Las circunferencias son exteriores.")
    elif d == (r1 + r2):
        print("Las circunferencias son tangentes exteriores.")
    elif d > abs(r1 - r2) and d < (r1 + r2):
        print("Las circunferencias son secantes.")
    elif d == abs(r1 - r2):
        print("Las circunferencias son tangentes interiores.")
    elif d < abs(r1 - r2):
        print("Las circunferencias son interiores.")
