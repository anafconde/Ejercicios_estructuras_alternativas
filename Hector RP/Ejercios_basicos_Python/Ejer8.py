sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese el valor de la primera venta: "))
venta2 = float(input("Ingrese el valor de la segunda venta: "))
venta3 = float(input("Ingrese el valor de la tercera venta: "))

comision = 0.10 * (venta1 + venta2 + venta3)
sueldo_total = sueldo_base + comision

print("Comisión total:", comision)
print("Sueldo total del mes:", sueldo_total)
