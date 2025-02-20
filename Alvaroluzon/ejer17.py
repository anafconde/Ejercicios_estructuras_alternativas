dado = int(input("Introduce el número obtenido en el dado (1-6): "))

if dado < 1 or dado > 6:
    print("ERROR: número incorrecto.")
else:
    if dado == 1:
        opuesta = "seis"
    elif dado == 2:
        opuesta = "cinco"
    elif dado == 3:
        opuesta = "cuatro"
    elif dado == 4:
        opuesta = "tres"
    elif dado == 5:
        opuesta = "dos"
    elif dado == 6:
        opuesta = "uno"
    
    print("En la cara opuesta está el \"" + opuesta + "\".")
