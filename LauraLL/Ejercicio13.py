#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

print("Para comprobar si la fecha es correcta, introduzca los siguientes datos...")
dia=int(input("Introduzca el día de la fecha a comprobar "))
mes=int(input("Introduzca el mes de la fecha a comprobar "))
anyo=int(input("Introduzca el año de la fecha a comprobar "))

#Comprobamos que el año es bisiesto o no
if ((anyo%4)==0 and (anyo%100)!=0) or (anyo%400)==0:
    if mes==2:
        if dia>=1 and dia<=29:
            print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es correcta")
        else:
            print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es INCORRECTA")
else:
    if mes>=1 and mes<=12:
        #Comprobamos los meses de 30 días para verificar el último paso, el día
        if mes==4 or mes==6 or mes==9 or mes==11:
            if dia>=1 and dia<=30:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es correcta")
            else:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es INCORRECTA")
        #Comprobamos el mes de febrero
        elif mes==2:
            if dia>=1 and dia<=28:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es correcta")
            else:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es INCORRECTA")
        #Comprobamos los meses con 31 días
        else:
            if dia>=1 and dia<=31:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es correcta")
            else:
                print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es INCORRECTA")
    else:
        print(f"La fecha introducida del año {anyo}, del mes {mes} y día {dia} es INCORRECTA")
