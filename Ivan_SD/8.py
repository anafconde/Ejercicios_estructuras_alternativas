

nota = float(input("Introduce tu nota: "))
edad = int(input("Introduce tu edad"))
sexo = str(input("Introduce tu sexo \"F\" o \"M\""))

if nota < 5 and edad < 18:
    print("No aceptada")
else:
    if sexo.upper == "F":
        print("ACEPTADA")
    elif sexo.upper == "M":
        print("POSIBLE")
    else:
        print(f"El género {sexo} no es válido")
