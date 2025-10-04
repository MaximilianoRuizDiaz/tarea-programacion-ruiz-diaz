# Ejercicio 7.7.8

def invertir_lista(lista):
    nueva = []
    for i in range(len(lista) - 1, -1, -1):
        nueva.append(lista[i])
    return nueva

def invertir_en_mismo_lugar(lista):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda < derecha:
        lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
        izquierda += 1
        derecha -= 1

# Prueba
l = ['Di', 'buen', 'día', 'a', 'papa']
print("Nueva lista invertida:", invertir_lista(l))
invertir_en_mismo_lugar(l)
print("Lista invertida en el mismo lugar:", l)
