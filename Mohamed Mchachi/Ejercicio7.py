# Autor: Mohamed Mchachi
# Versión: 1.1
# Enunciado:Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.


base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))


if exponente > 0:
    resultado = base ** exponente
elif exponente == 0:
    resultado = 1
else:
    resultado = 1 / (base ** abs(exponente))


print(f"El resultado de {base}^{exponente} es: {resultado}")
