# a) Enviar a todos
def votar_a_todos(tupla_nombres):
    for nombre in tupla_nombres:
        print("Estimado", nombre + ", vote por mí.")

# b) Enviar a una parte
def votar_a_partir(tupla_nombres, pos, cantidad):
    for i in range(pos, pos+cantidad):
        if i < len(tupla_nombres):
            print("Estimado", tupla_nombres[i] + ", vote por mí.")

# c) Diferenciar género
def votar_con_genero(lista_personas):
    for persona in lista_personas:
        nombre = persona[0]
        genero = persona[1]
        if genero == "M":
            print("Estimado", nombre + ", vote por mí.")
        else:
            print("Estimada", nombre + ", vote por mí.")

# Pruebas con nombres inventados
nombres = ("Juan", "María", "Pedro", "Ana")
personas = [("Juan","M"), ("María","F"), ("Pedro","M"), ("Ana","F")]

print("a) Todos:")
votar_a_todos(nombres)

print("\nb) A partir de la posición 1, 2 personas:")
votar_a_partir(nombres, 1, 2)

print("\nc) Con género:")
votar_con_genero(personas)
