# Author: Luis Palacios
# Version: 1.0

#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
# el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos 
# cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, 
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo,
# y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para 
# determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

tllamada=int(input("Tiempo de duración de la llamada: "))
dllamada=input("Que día realizó la llamada: ")
dllamada=dllamada.upper()

if dllamada == "DOMINGO" and tllamada <= 5:
    coste=1*1.03
    print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos un total de:",coste,"€")
elif dllamada == "DOMINGO" and 5 < tllamada <=8:
    coste=1.80*1.03
    print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos un total de:",coste,"€")
elif dllamada == "DOMINGO" and 8 < tllamada <= 10:
    coste=2.50*1.03
    print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos un total de:",coste,"€")
elif dllamada == "DOMINGO" and tllamada > 10:
    coste = 3*1.03
    print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos un total de:",coste,"€")
elif dllamada != "DOMINGO":
    turno=input("Has realizado la llamada en turno de mañana o tarde: ")
    turno=turno.upper()
    if turno == "MAÑANA" and tllamada <= 5:
        coste=1*1.15
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "MAÑANA" and 5 < tllamada <= 8:
        coste=1.80*1.15
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "MAÑANA" and 8 < tllamada <= 10:
        coste=2.50*1.15
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "MAÑANA" and tllamada > 10:
        coste=3*1.15
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "TARDE" and tllamada <= 5:
        coste=1*1.10
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "TARDE" and 5 < tllamada <= 8:
        coste=1.80*1.10
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "TARDE" and 8 < tllamada <= 10:
        coste=2.50*1.10
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
    elif turno == "TARDE" and tllamada > 10:
        coste=3*1.10
        print("Ha pagado por llamar el",dllamada,"durante",tllamada,"minutos, en turno de",turno,"un total de:",coste,"€")
else:
    print("Parámetros mal introducidos")
    