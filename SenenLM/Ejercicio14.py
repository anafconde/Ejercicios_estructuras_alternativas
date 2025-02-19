#version 1.0
#author Senén Lara
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
#la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
#ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
#considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos 
#si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
#Realice un algoritmo para determinar la ganancia obtenida.

#Meterle el precio inicial y los kilos para calcularlo
tamaño=int(input("Introduce el tamaño(1/2): "))
tipo=(input("Introduce el tipo de UVA(A/B): "))

if tipo == 'A':
    if tamaño == 1:
        suma1A = 20
    elif tamaño == 2:
        suma1B = 30
elif tipo == 'B':
    if tamaño == 1:
        suma2A = 30
    elif tamaño == 2:
        suma2B = 50
