# Diccionarios: Estructuras de datos que almacenan pares clave-valor.
# Se escriben entre llaves {} y los elementos están separados por comas.
# Son mutables, es decir, se pueden modificar sus elementos.
"""diccionario = {
    "nombre": "Nehuen",
    "edad": 25,
    "ciudad": "Buenos Aires",
    "es_estudiante": True,
}
consulta = diccionario["ciudad"]  # Accede al valor asociado a la clave "ciudad"

dic = {
    "fruta": ["manzana", "banana", "cereza"],
    "cantidad": 10,
    "precio": 2.5,
    "diccionario": {
        "nombre": "Nehuen",
        "edad": 25,
        "ciudad": "Buenos Aires",
        "es_estudiante": True,
    },
}

print(
    dic["fruta"][1]
)  # Accede al segundo elemento de la lista asociada a la clave "fruta"
print(
    dic["diccionario"]["nombre"]
)  # Accede al valor asociado a la clave "nombre" del diccionario anidado

prueba = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"], "c3": ["g", "h", "i"]}

letra = prueba["c2"][1]
print(letra.upper())
# print(prueba["c2"][1]).upper()  # no funciona

prueba["c4"] = ["j", "k", "l"]  # Agrega un nuevo par clave-valor al diccionario
print(prueba)
prueba["c4"] = ["s", "t", "u"]  # Modifica el valor asociado a la clave "c4"
print(prueba)

print(diccionario.keys())  # Devuelve una lista con las claves del diccionario
print(diccionario.values())  # Devuelve una lista con los valores del diccionario
print(diccionario.items())  # Devuelve una lista de tuplas con los pares clave-valor

for clave in diccionario:
    print(clave)"""


# Diccionario de un producto
producto = {"nombre": "Laptop HP", "precio": 1500.00, "stock": 25, "Disponible": True}

# Diccionario vacio
datos = {}

# Tambien se puede crear asi
persona = dict(nombre="Ana", edad=30, ciudad="Madrid")

# Acceder a valores
# Forma 1: Usando corchetes [] (genera error si la clave no existe)
# print(producto["nombre"])  # Accede al valor asociado a la clave "nombre"
# print(producto["categoria"])  # Genera un error si la clave no existe

# Forma 2: .get() (devuelve None si la clave no existe)
# print(producto.get("nombre"))  # Accede al valor asociado a la clave "nombre"
# print(producto.get("categoria"))  # Devuelve None si la clave no existe
# print(
#    producto.get("categoria", "No disponible")
# )  # Devuelve "No disponible" si la clave no existe

# Agregar o modificar valores
producto["categoria"] = "Electrónica"  # Agrega una nueva clave-valor
producto["precio"] = 1400.00  # Modifica el valor asociado a la clave "precio"

# Eliminar un par clave-valor
del producto["stock"]  # Elimina la clave "stock" y su valor asociado
# Eliminar y obtener el valor eliminado
precio_eliminado = producto.pop(
    "precio"
)  # Elimina la clave "precio" y devuelve su valor asociado

# print(producto)
# print("Precio eliminado:", precio_eliminado)

# Recorrer un diccionario
# Iterar sobre claves
for clave in producto:
    print(clave)
# Iterar sobre valores
for valor in producto.values():
    print(valor)
# Iterar sobre pares clave-valor
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
