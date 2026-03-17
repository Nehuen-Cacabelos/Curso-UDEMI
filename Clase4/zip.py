# Zip fuisona dos listas en una sola, creando tuplas con los elementos correspondientes de cada lista.

lista1 = [1, 2, 3, 4]
lista2 = ["a", "b", "c", "d"]
ciudades = ["Buenos Aires", "Madrid", "Londres", "París"]

combinados = list(
    zip(lista1, lista2, ciudades)
)  # Combina las tres listas en una sola, creando tuplas con los elementos correspondientes de cada lista. Si las listas tienen diferente longitud, se detiene al llegar al final de la lista más corta.
print(combinados)
