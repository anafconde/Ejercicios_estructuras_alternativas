# Author: Cris Moreno
# Version: 7.77
## Ejercicio 14 🍇
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
#la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la 
# venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto 
# recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: 
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
#  y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es 
# de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar 
# la ganancia obtenida.

PrecioKilocompra=float(1.50)
PrecioKilo=float(3.50)
kilos=float(input("¿Cuantos kilos se van a vender?: "))
tipo=input("De que tipo (A o B): ")
tamanyio=int(input("De que tamaño (1 o 2): " ))

if tipo=="A" and tamanyio==1:
    precio=float(kilos*(PrecioKilo+0.20))
    ganancia=float(precio-PrecioKilocompra*kilos)
    print(f"Obtienes una ganancia de {ganancia}€")
elif tipo=="A" and tamanyio==2:
    precio=float(kilos*(PrecioKilo+0.30))
    ganancia=float(precio-PrecioKilocompra*kilos)
    print(f"Obtienes una ganancia de {ganancia}€")
elif tipo=="B" and tamanyio==1:
    precio=float(kilos*(PrecioKilo-0.30))
    ganancia=float(precio-PrecioKilocompra*kilos)
    print(f"Obtienes una ganancia de {ganancia}€")
elif tipo=="B" and tamanyio==2:
    precio=float(kilos*(PrecioKilo-0.50))
    ganancia=float(precio-PrecioKilocompra*kilos)
    print(f"Obtienes una ganancia de {ganancia}€")
else:
    print("Introduce datos válidos.")






