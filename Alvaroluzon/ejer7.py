
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print(f"La potencia es: {resultado}")
elif exponente == 0:
    print("El resultado es: 1")
else:
    resultado = 1 / (base ** abs(exponente))
    print(f"La potencia es: {resultado}")
