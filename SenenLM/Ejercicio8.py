#version 1.0
#author Senén Lara

#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, 
# la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, 
# pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.


nota=int(input("Introduce la nota: "))
edad=int(input("Introduce la edad: "))
sexo=(input("Introduce el sexo (M/F): "))

if nota >= 5:
    if edad >= 18:
        if sexo == 'F':
            print("Aceptada")
        elif sexo == 'M':
            print("Posible")
else:
    print("No aceptada")


