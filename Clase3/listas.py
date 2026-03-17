# las listas se escriben entre corchetes [] y se pueden anidar elementos separados por comas
# las listas son mutables, es decir, se pueden modificar sus elementos

mi_lista = ["a", "b", "c", "f", "e"]  # lista de strings
"""otra_lista = ["Hola", 123, 45.6, True, [1, 2, 3]]  # lista con diferentes tipos de datos

resultado = mi_lista + otra_lista  # concatena las dos listas

resultado.append("f")  # agrega un elemento al final de la lista
resultado.remove("c")  # elimina el primer elemento con el valor especificado
resultado.pop(0)  # elimina y devuelve el último elemento de la lista

print(type(mi_lista))  # imprime <class 'list'>
print(mi_lista)  # imprime ['a', 'b', 'c', 'd', 'e']

print(resultado)  # imprime 5

print(mi_lista + otra_lista)  # concatena las dos listas
"""
mi_lista.sort()  # ordena la lista en orden ascendente no se puede guardar el resultado en otra variable
mi_lista.reverse()  # invierte el orden de la lista
print(mi_lista)  # imprime el primer elemento de la lista

lista = "Python"

una_lista = [
    n if n % 3 == 0 else "no" for n in range(0, 20, 2)
]  # lista de números del 0 al 20 con paso 2, si el número es divisible por 3 se agrega a la lista, sino se agrega "no"
print(una_lista)

pies = [10, 20, 30, 40, 50]
metros = [p / 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [p**2 for p in valores]

temperatura_fahrenheit = [32, 212, 275]
grados_celcius = [((p - 32) * (5 / 9)) for p in temperatura_fahrenheit]
print(grados_celcius)
