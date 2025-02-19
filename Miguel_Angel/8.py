#Author: Miguel Angel Garcia

#Version: 1.0
#Py Version : 3.11

#En este ejercicio pide un tipo de formulario para ingresar una nota, edad y sexo, si la nota es mayor 
# o igual a 5 y la edad es mayor o igual a 18, si el sexo es F se acepta, si el sexo es M es posible, si no es ninguno de los dos no se acepta.

nota = float(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (F/M): ").upper()

if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")