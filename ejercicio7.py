# Ejercicio 7.7.7

def formato_nombres(lista_tuplas):
    resultado = []
    for apellido, nombre, inicial in lista_tuplas:
        cadena = nombre + " " + inicial + ". " + apellido
        resultado.append(cadena)
    return resultado

# Prueba
tuplas = [("Perez", "Juan", "M"), ("Gomez", "Ana", "L")]
print("Formato nombres:", formato_nombres(tuplas))
