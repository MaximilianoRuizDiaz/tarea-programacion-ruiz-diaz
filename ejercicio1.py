def esta_ordenada(tupla):
    for i in range(len(tupla)-1):
        if tupla[i] > tupla[i+1]:
            return False
    return True

# Pruebas con salida descriptiva
tupla1 = (1, 2, 3, 4)
tupla2 = (4, 2, 3, 1)

print("Tupla:", tupla1, "-> Está ordenada?", esta_ordenada(tupla1))
print("Tupla:", tupla2, "-> Está ordenada?", esta_ordenada(tupla2))
