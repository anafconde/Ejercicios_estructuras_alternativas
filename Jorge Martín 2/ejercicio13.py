def es_fecha_valida(dia, mes, anio):
    import datetime
    try:
        datetime.datetime(anio, mes, dia)
        return "Fecha válida"
    except ValueError:
        return "Fecha inválida"

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

print(es_fecha_valida(dia, mes, anio))
