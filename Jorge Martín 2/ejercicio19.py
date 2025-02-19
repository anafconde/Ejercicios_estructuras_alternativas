def dias_en_mes(mes):
    dias = {
        1: 31, 2: "28 o 29 (si es bisiesto)", 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    return dias.get(mes, "ERROR: mes inválido.")

mes = int(input("Ingrese un número de mes (1-12): "))
print(f"El mes tiene {dias_en_mes(mes)} días.")
