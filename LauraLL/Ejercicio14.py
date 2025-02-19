#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida

print("----CALCULADORA DE GANANCIAS OBTENIDAS----")
print("1. Indicar el precio incial por kilo de la uva")
print("2. Indicar los kilos que se van a vender")
print("3. Indicar si es tipo A o tipo B")
print("4. Indicar el tamaño (1 | 2)")
print("-------------------------------------------")

#Recogida de datos
p_inicial=float(input("Indique el precio inicial: "))
kilos=float(input("Indique cuántos kilos va a vender: "))
tipo=input("Indique el tipo (A | B): ")
tamaño=int(input("Indique el tamaño (1 | 2): "))

#Compruebo que los valores de tipo y tamaño estén bien escritos
if (tipo != "A" and tipo != "B") or (tamaño != 1 and tamaño != 2):
    print("Error, uno de los valores introducidos no es válido")

#Hago la clasificación según el tipo y el tamaño
if tipo == "A":
    if tamaño == 1:
        total=((p_inicial+0.2)*kilos)
        print(f"El total de ganancias que obtendrá será de {total} €")
    else:
        total=((p_inicial+0.3)*kilos)
        print(f"El total de ganancias que obtendrá será de {total} €")

elif tipo == "B":
    if tamaño == 1:
        total=((p_inicial-0.3)*kilos)
        print(f"El total de ganancias que obtendrá será de {total} €")
    else:
        total=((p_inicial-0.5)*kilos)
        print(f"El total de ganancias que obtendrá será de {total} €")