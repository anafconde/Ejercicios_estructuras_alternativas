# Ejercicio 8
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ").upper()

if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("ACEPTADA")
    elif sexo == "M":
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")
