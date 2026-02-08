# es como una litra pero inmutable
# ocupan menos espacio en memoria
# se usan para datos que no van a cambiar
# es mas rapido que una lista

mi_tuple = (1, 2, 3, 4)
t = (5, 5.5, "Hola", True)

print(mi_tuple[1])  # Accede al primer elemento de la tupla

# Anidadas
tupla_anidada = (1, 2, (3, 4), [5, 6])
print(tupla_anidada[2][1])  # Accede al segundo elemento

# Castear una lista a tupla
otra_tupla = list(mi_tuple)
print(type(otra_tupla))

t = (1, 2, 3)
x, y, z = t  # Desempaquetado de tupla
print(x, y, z)  # Imprime: 1 2 3
print(
    t.count(1)
)  # el metodo count cuenta cuantas veces aparece un elemento en la tupla
print(
    t.index(2)
)  # el metodo index devuelve la posicion del elemento pasado como parametro
print(len(t))  # el metodo len devuelve la cantidad de elementos en la tupla
