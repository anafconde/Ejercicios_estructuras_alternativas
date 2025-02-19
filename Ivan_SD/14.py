

tipo = str(input("Introduce el tipo \"A\" o \"B\": "))
size = int(input("Introduce el tamaño \"1\" o \"2\": "))
tipo = tipo.upper()

if tipo == "A" and size == 1:
    print("Se cargarán .20€ por kilo")
elif tipo == "A" and size == 2:
    print("Se cargarán .30€ por kilo")
elif tipo == "B" and size == 1:
    print("Se rebajarán .30€ por kilo")
elif tipo == "B" and size == 2:
    print("Se rebajarán .50€ por kilo")
else:
    print("Opción no contemplada")
