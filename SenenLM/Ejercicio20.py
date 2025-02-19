#Una compañía de transporte internacional tiene servicio en algunos países de 
# América del Norte, América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.
# Lo anterior se muestra en la tabla:

#Zona	Ubicación	Costo/gramo
#1	América del Norte	24.00 euros
#2	América Central	20.00 euros
#3	América del Sur	21.00 euros
#4	Europa	10.00 euros
#5	Asia	18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
#esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro por la
#entrega de un paquete o, en su caso, el rechazo de la entrega.

#version 1.0
#author Senén Lara
print("1. America del Norte")
print("2. America Central")
print("3. America Del Sur")
print("4. Europa")
print("5. Asia")
pais=int(input("Introduce el pais donde se esta realizando la entrega (1-5): "))
peso_paquete = float(input("Introduce el peso del paquete en kilogramos: "))
if peso_paquete > 5:
    print("Rechazo: El paquete excede el límite de peso de 5 kg.")
else:
    peso_paquete_gramos = peso_paquete * 1000
    if pais == 1:
        costo_transporte = peso_paquete_gramos * 24.00  
    if pais == 2:
        costo_transporte = peso_paquete_gramos * 20.00  
    if pais == 3:
        costo_transporte = peso_paquete_gramos * 21.00  
    if pais == 4:
        costo_transporte = peso_paquete_gramos * 10.00  
    if pais == 5:
        costo_transporte = peso_paquete_gramos * 18.00  
print("El coste ha sido de",costo_transporte,"€")