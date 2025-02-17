#Autor: Juan Manuel López Torres
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

numero1=int(input("Indique el primer número: "))
numero2=int(input("Indique el segundo número: "))

if numero2 !=0:
    resultado= numero1/numero2
    print(f"El resultado de la división es: {resultado}")
else:
    print("La operación no se va a realizar use un 2º número que no sea 0.")
  
