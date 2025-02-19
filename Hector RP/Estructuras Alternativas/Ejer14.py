# Ejercicio 14
precio_inicial = float(input("Introduce el precio inicial por kilo (en euros): "))
tipo = input("Introduce el tipo de uva (A/B): ").upper()
tamano = input("Introduce el tamaño (1/2): ")
kilos = float(input("Introduce la cantidad de kilos entregados: "))

if tipo == "A":
    if tamano == "1":
        ajuste = 0.20
    elif tamano == "2":
        ajuste = 0.30
    else:
        ajuste = 0
elif tipo == "B":
    if tamano == "1":
        ajuste = -0.30
    elif tamano == "2":
        ajuste = -0.50
    else:
        ajuste = 0
else:
    ajuste = 0

precio_final = precio_inicial + ajuste
ganancia_total = precio_final * kilos

print("El productor recibirá un total de:", ganancia_total, "euros.")
