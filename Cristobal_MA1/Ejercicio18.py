# Author: Cris Moreno
# Version: 7.77
## Ejercicio 18 📅
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
#Si introducimos otro número nos da un error.

numeroDia=int(input("Dime un numero del 1 al 7, te dire a que dia de la semana corresponde: "))

if numeroDia==1:
    print(f"{numeroDia} corresponde al Lunes.")
elif numeroDia==2:
    print(f"{numeroDia} corresponde al Martes.")
elif numeroDia==3:
    print(f"{numeroDia} corresponde al Miercoles.")
elif numeroDia==4:
    print(f"{numeroDia} corresponde al Jueves.")
elif numeroDia==5:
    print(f"{numeroDia} corresponde al Viernes.")
elif numeroDia==6:
    print(f"{numeroDia} corresponde al Sabado.")
elif numeroDia<1 or numeroDia>7:
    print("Error. Introduce un numero del 1 al 7")
else:
    print(f"{numeroDia} corresponde al Domingo.")
