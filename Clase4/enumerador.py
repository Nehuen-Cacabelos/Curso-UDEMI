# Enumerado sirve para acceder a los indices de objetos iterables

lista = ["a", "b", "c"]

for item1, item in enumerate(range(50, 60, 2)):
    print(item1, item)

lista2 = list(enumerate(lista))
print(lista2[1][0])

# Lista con algunos nombres y por lo menos 3 cono la letra "M"
nombres = ["María", "Miguel", "Marta", "Carlos", "Ana"]

for indice, nombre in enumerate(nombres):
    letra = nombre[0]
    if letra == "M":
        print(indice)
