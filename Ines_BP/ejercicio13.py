#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

#Leer la fecha
dia=int(input("Introduce el día: "))
mes=int(input("Introduce el mes: "))
anyo=int(input("Introduce el año: "))

#Comprobación de dias
if anyo>=0 and anyo<=2100:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia>=1 and dia<=31:
            print(f"La fecha {dia}/{mes}/{anyo} es correcta")
        else:
            print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia >=1 and dia <=30:
            print(f"La fecha {dia}/{mes}/{anyo} es correcta")
        else:
            print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")
    elif mes==2: #SI EL MES ES FEBRERO COMPRUEBO SI EL AÑO ES BISIESTO
        if (anyo%4)==0: #SI EL AÑO ES DIVISIBLE ENTRE '4' PUEDE SER BISIESTO
            if (anyo%100)==0: #SI ES DIVISIBLE ENTRE '100' ES BISIESTO
                if (anyo%400)==0: # SI ES DIVISIBLE ENTRE '400' ES BISIESTO
                    if dia >=1 and dia <=29:
                        print(f"La fecha {dia}/{mes}/{anyo} es correcta")
                    else:
                        print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")
                else:
                    if dia >=1 and dia <=28:
                        print(f"La fecha {dia}/{mes}/{anyo} es correcta")
                    else:
                        print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")
            else:
                if dia >=1 and dia <=29:
                        print(f"La fecha {dia}/{mes}/{anyo} es correcta")
                else:
                    print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")
        else: #SI NO ES DIVISIBLE ENTRE '4' NO ES BISIESTO
            if dia >=1 and dia <=28:
                print(f"La fecha {dia}/{mes}/{anyo} es correcta")
            else:
                print(f"La fecha {dia}/{mes}/{anyo} NO es correcta")