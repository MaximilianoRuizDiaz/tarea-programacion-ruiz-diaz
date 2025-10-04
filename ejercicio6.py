# Ejercicio 7.7.6

def separar_por_k(lista, k):
    menores = []
    iguales = []
    mayores = []
    for num in lista:
        if num < k:
            menores.append(num)
        elif num == k:
            iguales.append(num)
        else:
            mayores.append(num)
    return menores, iguales, mayores

def multiplos_de_k(lista, k):
    multiplos = []
    for num in lista:
        if num % k == 0:
            multiplos.append(num)
    return multiplos

# Prueba
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Separar por k:", separar_por_k(lista, 5))
print("Múltiplos de k:", multiplos_de_k(lista, 3))
