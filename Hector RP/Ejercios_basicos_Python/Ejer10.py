nota1 = float(input("Ingrese la primera nota parcial: "))
nota2 = float(input("Ingrese la segunda nota parcial: "))
nota3 = float(input("Ingrese la tercera nota parcial: "))
examen = float(input("Ingrese la nota del examen final: "))
trabajo = float(input("Ingrese la nota del trabajo final: "))

promedio_parciales = (nota1 + nota2 + nota3) / 3
nota_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)
print("La nota final es:", nota_final)
