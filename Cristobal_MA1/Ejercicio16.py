# Author: Cris Moreno
# Version: 7.77
## Ejercicio 16 📞

# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
# el cobro es por el tiempo que ésta dura, de tal forma que: 
# - los primeros cinco minutoscuestan 1 euro 
# - los siguientes tres, 80 céntimos 
# - los siguientes dos minutos, 70 céntimos
# - a partir del décimo minuto, 50 céntimos. 
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
# en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice
# un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza
# una llamada.

print("=-Calcula el precio de tu llamada=-")

minutos=int(input("¿Cuantos minutos ha durado la llamada?: "))
dia=input("¿Que dia de la semana?: ")
turno=input("¿En que turno comenzó la llamada? (Mañana de 7H a 14H, Tarde de 15H a 6H): ")

conceptoMinutos=float(0)

#Llamadas en DOMINGO
if minutos<=5 and dia=="Domingo":
    conceptoMinutos=float((minutos*1)*1.03)
elif minutos>5 and minutos<=8 and dia=="Domingo":
    conceptoMinutos=float(((minutos-5)*0.80+5)*1.03)
elif minutos>5 and minutos<=10 and dia=="Domingo":
    conceptoMinutos=float(((minutos-8)*0.70+(0.80*3+5))*1.03)
elif minutos>10 and dia=="Domingo":
    conceptoMinutos=float(((minutos-10)*0.5+(0.80*3+5+1.40))*1.03)

#Llamadas en NO-DOMINGO por la MAÑANA
elif minutos<=5 and dia!="Domingo" and turno=="Mañana":
    conceptoMinutos=float((minutos*1)*1.15)
elif minutos>5 and minutos<=8 and dia!="Domingo" and turno=="Mañana":
    conceptoMinutos=float(((minutos-5)*0.80+5)*1.15)
elif minutos>5 and minutos<=10 and dia!="Domingo" and turno=="Mañana":
    conceptoMinutos=float(((minutos-8)*0.70+(0.80*3+5))*1.15)
elif minutos>10 and dia!="Domingo" and turno=="Mañana":
    conceptoMinutos=float(((minutos-10)*0.5+(0.80*3+5+1.40))*1.15)

#Lamadas en NO-DOMINGO por la TARDE
elif minutos<=5 and dia!="Domingo" and turno=="Tarde":
    conceptoMinutos=float((minutos*1)*1.10)
elif minutos>5 and minutos<=8 and dia!="Domingo" and turno=="Tarde":
    conceptoMinutos=float(((minutos-5)*0.80+5)*1.10)
elif minutos>5 and minutos<=10 and dia!="Domingo" and turno=="Tarde":
    conceptoMinutos=float(((minutos-8)*0.70+(0.80*3+5))*1.10)
elif minutos>10 and dia!="Domingo" and turno=="Tarde":
    conceptoMinutos=float(((minutos-10)*0.5+(0.80*3+5+1.40))*1.10)



print(f"La llamada cuesta {conceptoMinutos}€")

