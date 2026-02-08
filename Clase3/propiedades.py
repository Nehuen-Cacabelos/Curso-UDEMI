nombre = "Carina"
# nombre[0] = "K"  # Esto generará un error porque las cadenas son inmutables
n1 = "Kari"
n2 = "na"

print((n1 + n2) * 10)  # Concatenación de cadenas

poema = """Hola, Mundo!"""

print("Hola" in poema)  # Verifica si "agua" está en el poema, devuelve True o False
print(
    "sol" not in poema
)  # Verifica si "sol" no está en el poema, devuelve True o False
print("sol" in poema)  # Verifica si "sol" está en el poema, devuelve True o False

print(len(poema))  # Devuelve la longitud del string
