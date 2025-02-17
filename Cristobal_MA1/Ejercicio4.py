# Author: Cris Moreno
# Version: 7.77
# Crea un programa que pida al usuario dos números y muestre su división si el segundo 
# no es cero, o un mensaje de aviso en caso contrario.

num1=int(input("Dime un numero: "))
num2=int(input("Dime otro numero: "))

if num2==0:
    print("El segundo numero no puede ser cero.")
else:
    division=num1/num2
    print("El resultado de la division es", division)

