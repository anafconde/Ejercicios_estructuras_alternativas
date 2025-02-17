#Version
#Enunciado del algoritmo

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)
print(f"Los números ordenados de mayor a menor son: {numeros}")
