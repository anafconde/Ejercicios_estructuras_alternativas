# Ejercicio 20
peso = float(input("Introduce el peso del paquete en kilogramos: "))

if peso > 5:
    print("El paquete no puede ser transportado.")
else:
    print("Zonas disponibles:")
    print("1: América del Norte")
    print("2: América Central")
    print("3: América del Sur")
    print("4: Europa")
    print("5: Asia")
    zona = int(input("Introduce la zona (1-5): "))

    if zona == 1:
        costo_por_gramo = 24.00
    elif zona == 2:
        costo_por_gramo = 20.00
    elif zona == 3:
        costo_por_gramo = 21.00
    elif zona == 4:
        costo_por_gramo = 10.00
    elif zona == 5:
        costo_por_gramo = 18.00
    else:
        print("Zona no válida.")
        costo_por_gramo = None

    if costo_por_gramo is not None:
        gramos = peso * 1000
        total = gramos * costo_por_gramo
        print("El cobro por el servicio es:", total, "euros.")
