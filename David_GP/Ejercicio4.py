# Version 1.0
# Autor David García Pérez

#Ejercicio 4
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

numero1=float(input("Introduce el primer número: "))
numero2=float(input("Introduce el segundo número: "))

if numero2 != 0:
  division=numero1/numero2
  print("La división de", numero1, "entre", numero2, "es:", division)
else:
  print("No se puede dividir entre cero")