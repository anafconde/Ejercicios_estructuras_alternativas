#-----Autor:Israel
#-----Version:V1-----------
#---Enunciado del algoritmo
#Escribe un programa que lea un número e indique si es par o impar

n=float(input("Introduce un número: "))

resto=n%2

if resto==0:
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")