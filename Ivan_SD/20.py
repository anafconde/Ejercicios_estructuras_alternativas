

print("1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia\n")

zona = int(input("Introduce la zona : "))
peso = int(input("Introduce los kilos: "))
peso *= 1000

if peso > 5000:
    print("Un paquete no puede superar los 5 KG")
    exit(1)

if zona == 1:
    peso *= 24
    print(f"El precio final es {peso}€")
elif zona == 2:
    peso *= 20
    print(f"El precio final es {peso}€")
elif zona == 3:
    peso *= 21
    print(f"El precio final es {peso}€")
elif zona == 4:
    peso *= 10
    print(f"El precio final es {peso}€")
elif zona == 5:
    peso *= 18
    print(f"El precio final es {peso}€")








