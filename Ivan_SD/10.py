

from math import sqrt

x1 = float(input("Dime el eje x del primer círculo: "))
y1 = float(input("Dime el eje y del primer círculo: "))
r1 = float(input("Dime el radio del primer círculo: "))

x2 = float(input("Dime el eje x del segundo círculo: "))
y2 = float(input("Dime el eje y del segundo círculo: "))
r2 = float(input("Dime el radio del segundo círculo: "))

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance > r1 + r2:
    print("Es exterior")
elif distance == r1 + r2:
    print("Es tangente exterior")
elif distance < r1 + r2 and distance > abs(r1 - r2):
    print("Es secante")
elif distance == abs(r1 -r2):
    print("Es tangente interior")
elif distance < abs(r1 - r2):
    print("Es interior")
elif distance == 0 and r1 == r2:
    print("Es concéntrica")
else:
    print("Opción no contemplada")
