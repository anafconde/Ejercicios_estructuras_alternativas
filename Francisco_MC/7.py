#Version
#Enunciado del algoritmo

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    print(f"La potencia es: {base ** exponente}")
elif exponente == 0:
    print("El resultado es 1.")
else:
    print(f"El resultado es: {1 / (base ** abs(exponente))}")
