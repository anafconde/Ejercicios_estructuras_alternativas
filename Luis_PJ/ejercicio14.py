# Author: Luis Palacios
# Version: 1.0

# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
# se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial 
# cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos 
# cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

precioini=float(input("Introduce el precio inicial del kilo de uva: "))
tipo=input("Introduce el tipo de uva: 'A' o 'B': ")
tamaño=int(input("Indica el tamaño de la uva: '1' ó '2': "))
kilo=float(input("Introduce el numero de kilos de uva: "))
tipo=tipo.upper()

if tipo == 'A' and tamaño == 1:
    preciofinal=precioini+0.20
    pago=preciofinal*kilo
    print("El precio de la uva se paga a",preciofinal,"€/kilo y ha obtenido una ganacia de",pago,"€")
elif tipo == 'A' and tamaño == 2:
    preciofinal=precioini + 0.30
    pago=preciofinal*kilo
    print("El precio de la uva se paga a",preciofinal,"€/kilo y ha obtenido una ganacia de",pago,"€")
elif tipo =='B' and tamaño == 1:
    preciofinal=precioini-0.30
    pago=preciofinal*kilo
    print("El precio de la uva se paga a",preciofinal,"€/kilo y ha obtenido una ganacia de",pago,"€")
elif tipo == 'B' and tamaño == 2:
    preciofinal=precioini-0.50
    pago=preciofinal*kilo
    print("El precio de la uva se paga a",preciofinal,"€/kilo y ha obtenido una ganacia de",pago,"€")
else:
    print("No has introducido los valores correctamente")


