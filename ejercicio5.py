# a) Números primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def lista_primos(lista):
    resultado = []
    for num in lista:
        if es_primo(num):
            resultado.append(num)
    return resultado

# b) Suma y promedio
def suma_y_promedio(lista):
    suma = 0
    for num in lista:
        suma += num
    promedio = suma / len(lista)
    return suma, promedio

# c) Factoriales
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def lista_factoriales(lista):
    resultado = []
    for num in lista:
        resultado.append(factorial(num))
    return resultado

# Pruebas con salida clara
numeros = [1, 2, 3, 4, 5, 6, 7]

print("Lista:", numeros)
print("a) Primos en la lista:", lista_primos(numeros))

suma, prom = suma_y_promedio(numeros)
print("b) Suma:", suma, "Promedio:", prom)

print("c) Factoriales de la lista:", lista_factoriales([3,4,5]))
