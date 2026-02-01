texto = "Este es un texto de ejemplo para metodos de string."
"""
texto = texto.upper()  # Convierte todo a mayusculas
texto = texto.lower()  # Convierte todo a minusculas
texto = (
    texto.split()
)  # Divide el string en una lista de palabras, se puede pasar parametros para definir el separador

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join(
    [a, b, c, d]
)  # Une una lista de strings en un solo string, usando el string original como separador
f = "!"
"""
resultado = texto.find(
    "w"
)  # Busca la primera ocurrencia de "u", devuelve -1 si no lo encuentra a diferencia de index

resultado = texto.replace(
    "texto", "frase"
)  # Reemplaza todas las ocurrencias de "texto" por "frase"

resultado = texto.replace("e", "3")  # Reemplaza todas las ocurrencias de "e" por "3"

print(resultado)
# print(e + f)
