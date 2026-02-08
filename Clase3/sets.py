# los sets se declaran de dos maneras
# usando llaves {}
# conjunto = {1, 2, 3, 4, 5}
# usando la funcion set()
# otro_conjunto = set([4, 5, 6, 7, 8])

# los elementos no se pueden repetir
# estos no se pueden indexar ni ordenar
# son mutables, se pueden agregar o eliminar elementos
# no inlcuyen listas, diccionarios u otros sets como elementos


otro_set = set((4, 5, 6, 7, 8))
print(type(otro_set))
print(otro_set)

mi_set = {1, 2, 3, 4, (1, 2, 3), 6}  # los elementos repetidos se ignoran
# permite sets anidados si se usan tuplas porque son inmutables
print(mi_set)
print(len(mi_set))  # devuelve la cantidad de elementos en el set
print(3 in mi_set)  # verifica si un elemento esta en el set

# metodos
mi_set.add(7)  # agrega un elemento al set
mi_set.remove(2)  # elimina un elemento del set, genera error si no existe
mi_set.discard(10)  # elimina un elemento del set, no genera error si no existe
# mi_set.pop()  # elimina y devuelve un elemento aleatorio del set
s1 = mi_set.pop()
print("Elemento eliminado:", s1)
mi_set.clear()  # elimina todos los elementos del set
print(mi_set)
# concatenar dos sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = set_a.union(set_b)  # union de dos sets
