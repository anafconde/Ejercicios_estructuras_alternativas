# Author: Cris Moreno
# Version: 7.77
## Ejercicio 20 📦
#Una compañía de transporte internacional tiene servicio en algunos países de América 
#del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de 
#transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se 
#muestra en la tabla:

#| Zona | Ubicación          | Costo/gramo |
#|------|--------------------|-------------|
#| 1    | América del Norte  | 24.00 euros |
#| 2    | América Central    | 20.00 euros |
#| 3    | América del Sur    | 21.00 euros |
#| 4    | Europa             | 10.00 euros |
#| 5    | Asia               | 18.00 euros |

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son 
# transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo 
# para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la 
# entrega.
print("-=Calculo de tarifa de envio=-")
peso=float(input("Introduce el peso del paquete (En Kg): "))
print("1-America del Norte, 2-America Central, 3-America del Sur, 4-Europa, 5-Asia")
zona=int(input("Introduce la zona de destino del paquete (Numero de Zona): "))

peso=float(peso*1000)
if peso <= 5000 and zona ==1:
    precio=peso*24
    print(f"El precio de tu envio será de {precio}€")
elif peso <= 5000 and zona ==2:
    precio=peso*20
    print(f"El precio de tu envio será de {precio}€")
elif peso <= 5000 and zona ==3:
    precio=peso*21
    print(f"El precio de tu envio será de {precio}€")
elif peso <= 5000 and zona ==4:
    precio=peso*10
    print(f"El precio de tu envio será de {precio}€")
elif peso <= 5000 and zona ==5:
    precio=peso*18
    print(f"El precio de tu envio será de {precio}€")
elif peso > 5000:
    print("No podemos enviar paquetes de mas de 5Kg.")



