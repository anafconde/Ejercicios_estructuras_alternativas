a = float(input("Introduce el lado A: "))
b = float(input("Introduce el lado B: "))
c = float(input("Introduce el lado C: "))

if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("El triángulo es rectángulo.")
elif a == b and b == c:
    print("El triángulo es equilátero.")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
