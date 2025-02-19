#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos,
# 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
# en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar 
# por cada concepto una persona que realiza una llamada.
#version 1.0
#author Senén Lara

tiempollamada=float(input("Introduce los minutos en llamada: "))
costellamada = 0.0
if tiempollamada <= 5:
    costellamada = tiempollamada * 100
elif tiempollamada <= 8:
    costellamada = (5 * 100) + ((tiempollamada - 5) * 80)
elif tiempollamada <= 10:
    costellamada = (5 * 100) + (3 * 80) + ((tiempollamada - 8) * 70)
elif tiempollamada > 10:
    costellamada = (5 * 100) + (3 * 80) + (2 * 70) + ((tiempollamada - 10) * 50)

print(costellamada)
dia=input("Introduce el dia de la llamada: ")
momento=input("Introduce el momento del dia de la llamada: ")
if dia == 'Domingo':
    costellamada=costellamada*1.03
else:
    if momento == 'Mañana':
        costellamada == costellamada*1.15
    elif momento == 'Tarde':
        costellamada == costellamada*1.10
costellamada=round(costellamada/100, 2)
print ("La llamada ha costado: ",costellamada,"€")
    
    