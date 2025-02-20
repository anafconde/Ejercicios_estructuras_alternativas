#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega

print("----COMPAÑÍA DE TRANSPORTES LINARES----")
print("1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia")
print("----------------------------------------")

opc=int(input("Introduzca el número de la opción a elegir: "))

peso=float(input("Introduzca el peso (en kilogramos) del paquete a enviar: "))
peso=float(peso*1000)

if peso>5000:
    print("El peso supera el excedido")
else:
    if opc==1:
        coste=peso*24
        print(f"El coste del envío de su paquete a América del Norte será de {coste} €")
    elif opc==2:
        coste=peso*20
        print(f"El coste del envío de su paquete a América Central será de {coste} €")
    elif opc==3:
        coste=peso*21
        print(f"El coste del envío de su paquete a América del Sur será de {coste} €")
    elif opc==4:
        coste=peso*10
        print(f"El coste del envío de su paquete a Europa será de {coste} €")
    elif opc==5:
        coste=peso*18
        print(f"El coste del envío de su paquete a Asia será de {coste} €")
    else:
        print("Valor introducido incorrecto")