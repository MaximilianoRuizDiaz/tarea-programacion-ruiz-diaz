# a) Producto escalar
def producto_escalar(v1, v2):
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    return resultado

# b) Ortogonales
def son_ortogonales(v1, v2):
    return producto_escalar(v1, v2) == 0

# c) Paralelos
def son_paralelos(v1, v2):
    razon = None
    for i in range(len(v1)):
        if v2[i] != 0:
            if razon is None:
                razon = v1[i]/v2[i]
            elif v1[i]/v2[i] != razon:
                return False
        else:
            if v1[i] != 0:
                return False
    return True

# d) Norma
def norma_vector(v):
    suma = 0
    for i in v:
        suma += i**2
    return suma**0.5

# Pruebas con salida clara
v1 = [1, 2]
v2 = [3, 4]
v3 = [2, 4]
v4 = [1, 2]

print("Vectores:", v1, v2, "-> Producto escalar:", producto_escalar(v1, v2))
print("Vectores [1,0] y [0,1] -> Ortogonales?", son_ortogonales([1,0],[0,1]))
print("Vectores:", v3, v4, "-> Paralelos?", son_paralelos(v3, v4))
print("Norma del vector [3,4]:", norma_vector([3,4]))
# a) Producto escalar
def producto_escalar(v1, v2):
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    return resultado

# b) Ortogonales
def son_ortogonales(v1, v2):
    return producto_escalar(v1, v2) == 0

# c) Paralelos
def son_paralelos(v1, v2):
    razon = None
    for i in range(len(v1)):
        if v2[i] != 0:
            if razon is None:
                razon = v1[i]/v2[i]
            elif v1[i]/v2[i] != razon:
                return False
        else:
            if v1[i] != 0:
                return False
    return True

# d) Norma
def norma_vector(v):
    suma = 0
    for i in v:
        suma += i**2
    return suma**0.5

# Pruebas con salida clara
v1 = [1, 2]
v2 = [3, 4]
v3 = [2, 4]
v4 = [1, 2]

print("Vectores:", v1, v2, "-> Producto escalar:", producto_escalar(v1, v2))
print("Vectores [1,0] y [0,1] -> Ortogonales?", son_ortogonales([1,0],[0,1]))
print("Vectores:", v3, v4, "-> Paralelos?", son_paralelos(v3, v4))
print("Norma del vector [3,4]:", norma_vector([3,4]))
