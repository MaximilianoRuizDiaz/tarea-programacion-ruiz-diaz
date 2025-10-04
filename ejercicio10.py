# Ejercicio 7.7.10

def sumar_matrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

def multiplicar_matrices(m1, m2):
    filas_m1 = len(m1)
    cols_m1 = len(m1[0])
    cols_m2 = len(m2[0])
    resultado = []
    for i in range(filas_m1):
        fila = []
        for j in range(cols_m2):
            suma = 0
            for k in range(cols_m1):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def matriz_triangular_superior(matriz):
    n = len(matriz)
    m = [fila[:] for fila in matriz]  # copia simple
    for i in range(n):
        for j in range(i+1, n):
            if m[i][i] != 0:
                factor = m[j][i] / m[i][i]
                for k in range(len(m[j])):
                    m[j][k] = m[j][k] - factor * m[i][k]
    return m

def son_vectores_independientes(lista_vectores):
    for v in lista_vectores:
        if all(x == 0 for x in v):  # vector nulo
            return False
    for i in range(len(lista_vectores)):
        for j in range(i+1, len(lista_vectores)):
            if lista_vectores[i] == lista_vectores[j]:  # repetido
                return False
    return True

# Pruebas
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print("Suma de matrices:", sumar_matrices(m1, m2))
print("Producto de matrices:", multiplicar_matrices(m1, m2))
print("Matriz triangular superior:", matriz_triangular_superior([[2, 1], [4, 3]]))
print("Vectores independientes:", son_vectores_independientes([[1, 0], [0, 1], [1, 1]]))
