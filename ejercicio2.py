# a) Con tuplas
def encajan_tuplas(ficha1, ficha2):
    return ficha1[0] in ficha2 or ficha1[1] in ficha2

# b) Con cadenas
def encajan_cadenas(f1, f2):
    ficha1 = f1.split("-")
    ficha2 = f2.split("-")
    ficha1 = (int(ficha1[0]), int(ficha1[1]))
    ficha2 = (int(ficha2[0]), int(ficha2[1]))
    return encajan_tuplas(ficha1, ficha2)

# Pruebas con salida clara
f1, f2 = (3,4), (5,4)
print("Fichas (tuplas):", f1, "y", f2, "-> Encajan?", encajan_tuplas(f1, f2))

f3, f4 = "3-4", "5-4"
print("Fichas (cadenas):", f3, "y", f4, "-> Encajan?", encajan_cadenas(f3, f4))
