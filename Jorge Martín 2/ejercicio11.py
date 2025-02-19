def clasificar_triangulo(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Triángulo Rectángulo"
    elif a == b and b == c:
        return "Triángulo Equilátero"
    elif a == b or b == c or a == c:
        return "Triángulo Isósceles"
    else:
        return "Triángulo Escaleno"

a = int(input("Ingrese el lado A: "))
b = int(input("Ingrese el lado B: "))
c = int(input("Ingrese el lado C: "))

print("El triángulo es:", clasificar_triangulo(a, b, c))
