"""monedas = 5

while monedas > 0:
    print(f"Tienes un total de {monedas} monedas.")
    monedas -= 1
else:
    print("no tengo mas monedas")

respuesta = "s"

while respuesta == "s":
    respuesta = input("Quiere seguir? (s/n)")
else:
    print("Gracias")"""

# Break interrumpe el loop
# Continue saltea la interacion y sigue con la siguiente
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "h":
        continue
    print(letra)
