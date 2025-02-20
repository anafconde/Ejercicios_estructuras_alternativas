

n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

if n2 == 0:
    print("El segundo número no puede ser 0")
    exit(1)
n1 /= n2
print(f"El resultado es {n1}")