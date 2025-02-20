# Version 1.0
# Autor David García Pérez

#Ejercicio 14
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

def calcular_ganancia(precio_inicial, tipo, tamaño):
    # Ajuste según el tipo y tamaño de la uva
    if tipo == 'A':
        if tamaño == 1:
            precio_final = precio_inicial + 0.20  # 20 céntimos
        elif tamaño == 2:
            precio_final = precio_inicial + 0.30  # 30 céntimos
        else:
            print("Tamaño inválido")
    elif tipo == 'B':
        if tamaño == 1:
            precio_final = precio_inicial - 0.30  # 30 céntimos menos
        elif tamaño == 2:
            precio_final = precio_inicial - 0.50  # 50 céntimos menos
        else:
            print("Tamaño inválido")
    else:
        print("Tipo inválido")

    print(f"El precio final por kilo de uva es: {precio_final} €")

# Solicitar datos al usuario
precio_inicial = float(input("Ingrese el precio inicial por kilo de uva: "))
tipo = input("Ingrese el tipo de uva (A o B): ").upper()
tamaño = int(input("Ingrese el tamaño de la uva (1 o 2): "))

# Calcular la ganancia y mostrar el resultado
calcular_ganancia(precio_inicial, tipo, tamaño)