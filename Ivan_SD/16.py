

sum = 0
min = float(input("Introduce los minutos que duró la llamada: "))
dom = str(input("¿Hoy es domingo? (Si o no): "))
dom.lower()

if min >= 5:
    sum+=1
if min >= 8:
    sum+=0.8
if min >= 10:
    sum+=0.7
if min > 10:
    min -= 10

sum += min*0.5

if dom == "si":
    sum += sum * 0.03
    round(sum,2)
    print(f"El resultado final es {sum}")
elif dom == "no":
    turn = str(input("Turno de mañana o tarde: "))
    turn.lower()

    if turn == "mañana":
        sum += sum * 0.15
        round(sum,2)
        print(f"El resultado final es {sum}")
    elif turn == "tarde":
        sum += sum * 0.10
        round(sum,2)
        print(f"El resultado final es {sum}")
    else:
        print("Opción no contemplada")
else:
    print("Opción no contemplada")