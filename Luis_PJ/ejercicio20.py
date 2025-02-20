# Author: Luis Palacios
# Version: 1.0

# Una compañía de transporte internacional tiene servicio en algunos países de 
# América del Norte, América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete 
# y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
# Zona // Ubicación // Costo/gramo
# 1 // America del Norte // 24.00 euros
# 2 // America Central // 20.00 euros
# 3 // America del Sur // 21.00 euros
# 4 // Europa // 10.00 euros
# 5 // Asia // 18.00 euros

# Parte de su política implica que los paquetes con un peso superior a 5 kg
# no son transportados, esto por cuestiones de logística y de seguridad. 
# Realice un algoritmo para determinar el cobro por la entrega de un 
# paquete o, en su caso, el rechazo de la entrega.

ubicacion=int(input("Introduce del 1 al 5, la zona para enviar el paquete: "))
peso=float(input("Introduce el peso del paquete que vas a enviar en kg: "))
pgramos=peso*1000

if ubicacion == 1 and pgramos <= 5000:
    coste=pgramos * 24
    print("Su pedido en América del norte vale:",coste,"€")
elif ubicacion == 2 and pgramos <= 5000:
    coste=pgramos * 20
    print("Su pedido en América Central vale:",coste,"€")
elif ubicacion == 3 and pgramos <= 5000:
    coste=pgramos * 21
    print("Su pedido en América del Sur vale:",coste,"€")
elif ubicacion == 4 and pgramos <= 5000:
    coste=pgramos * 10
    print("Su pedido en Europa vale:",coste,"€")
elif ubicacion == 5 and pgramos <= 5000:
    coste=pgramos * 18
    print("Su pedido en Asia vale:",coste,"€")
else:
    if ubicacion < 1 or ubicacion > 5:
        print("ERROR. Ubicación mal introducida")
    elif pgramos > 5000:
        print("Por seguridad no repartimos paquetes de ese peso")

