num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

numeros_ordenados = sorted([num1, num2, num3], reverse=True)
print("Números ordenados de mayor a menor:", numeros_ordenados)
