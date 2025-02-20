#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada

t_llamada=float(input("Introduzca el tiempo que duró su llamada: "))

if t_llamada>=0 and t_llamada<=5:
    costo=t_llamada*100
elif t_llamada>5 and t_llamada<=8:
    costo=(t_llamada-5)*80
    costo=costo+(5*100)
elif t_llamada>8 and t_llamada<=10:
    costo=(t_llamada-8)*70
    costo=costo+(5*100)+(3*80)
elif t_llamada>10:
    costo=(t_llamada-10)*50
    costo=costo+(5*100)+(3*80)+(2*70)

dia_llamada=input("¿Cuándo se realizó la llamada? (mañana | tarde | domingo) ")

if dia_llamada == "mañana":
    cargo=(costo*1.15)/100
    print(f"El cargo por su llamada de {t_llamada} es de {cargo} €")
elif dia_llamada == "tarde":
    cargo=(costo*1.1)/100
    print(f"El cargo por su llamada de {t_llamada} es de {cargo} €")
elif dia_llamada == "domingo":
    cargo=(costo*1.03)/100
    print(f"El cargo por su llamada de {t_llamada} es de {cargo} €")
else:
    print("Valor introducido no válido")