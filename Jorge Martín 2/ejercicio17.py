def cara_opuesta_dado(numero):
    if numero < 1 or numero > 6:
        return "ERROR: número incorrecto."
    
    opuesta = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    nombres = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis"}
    
    return f"En la cara opuesta está el \"{nombres[opuesta[numero]]}\"."

numero = int(input("Introduce número del dado: "))
print(cara_opuesta_dado(numero))
