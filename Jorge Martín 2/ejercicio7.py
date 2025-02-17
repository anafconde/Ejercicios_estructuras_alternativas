base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
elif exponente == 0:
    resultado = 1
else:
    resultado = 1 / (base ** abs(exponente))

print(f"El resultado es: {resultado}")

