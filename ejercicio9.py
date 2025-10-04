# Ejercicio 7.7.9

def empaquetar(lista):
    if not lista:
        return []
    resultado = []
    valor_actual = lista[0]
    contador = 1
    for i in range(1, len(lista)):
        if lista[i] == valor_actual:
            contador += 1
        else:
            resultado.append((valor_actual, contador))
            valor_actual = lista[i]
            contador = 1
    resultado.append((valor_actual, contador))
    return resultado

# Prueba
print("Empaquetar:", empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))
