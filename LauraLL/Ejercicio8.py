#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’

nota=float(input("Introduzca la nota: "))
edad=int(input("Introduzca la edad: "))
sexo=input("Introduzca el sexo (F/M): ")

if nota>=5 and edad>=18:
    if sexo=="F":
        print("ACEPTADA")
    else:
        print("POSIBLE")
else:
    print("NO ACEPTADA/O")