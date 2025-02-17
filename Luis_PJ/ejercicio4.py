# Author: Luis Palacios
# Version: 1.0

# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce otro numero: "))

if numero2!=0:
    division=numero1/numero2
    print("El resultado de la division es",division)
else:
    print("Error division no posible")