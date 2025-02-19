# Version 1.0
# Autor David García Pérez

#Ejercicio 20
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

#Zona	Ubicación	Costo/gramo
#1	América del Norte	24.00 euros
#2	América Central	20.00 euros
#3	América del Sur	21.00 euros
#4	Europa	10.00 euros
#5	Asia	18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

def calcular_costo_envio(peso, zona):
#Calcula el costo de envío basado en el peso del paquete y la zona de destino.
    
# Verificar si el peso es válido (menor o igual a 5 kg)
    if peso > 5000:
        return "ERROR: Paquete rechazado, peso superior a 5 kg."
    
# Tabla de costos por zona (en euros por gramo)
    costos_por_zona = {
        1: 24.00,  # América del Norte
        2: 20.00,  # América Central
        3: 21.00,  # América del Sur
        4: 10.00,  # Europa
        5: 18.00   # Asia
    }

# Verificar si la zona es válida
    if zona not in costos_por_zona:
        return "ERROR: Zona incorrecta."
    
# Calcular el costo total (costo por gramo * peso del paquete)
    costo = costos_por_zona[zona] * peso
    
    return f"El costo del envío es: {costo:.2f} euros."

# Solicitar los datos al usuario
peso = float(input("Introduce el peso del paquete en gramos: "))
zona = int(input("Introduce el número de zona (1-5): "))

# Calcular y mostrar el costo o el error
resultado = calcular_costo_envio(peso, zona)
print(resultado)