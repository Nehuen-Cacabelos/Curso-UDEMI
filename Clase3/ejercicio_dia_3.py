# crear un programa que le pida al usuario un texto, luego  que ingrese 3 letras a eleccion. son 5 analisis que debe hacer el programa:
# 1- contar cuantas veces aparece cada letra en el texto
# guardar en lista y con un metodo contar cuantas veces aparece cada letra
# 2- cuantas palabras tiene el texto
# 3 cual es la primer y ultima letra del texto
# 4 mostrar como queda el texto si se invierte el orden de las palabras
# 5 = mostrar si el texto tiene la palabra "python" (true o false)

# Ingreso de texto
texto = input("Ingrese un texto: ").lower()

# Separacion de letras y armado de la lista
letras = input("Ingrese 3 letras: ").lower()
letras = letras.split()

print("\n")
# Cuenta la cantidad de letras
print("Cantidad de letras")

cant_1 = texto.count(letras[0])
cant_2 = texto.count(letras[1])
cant_3 = texto.count(letras[2])

print(
    f"La cantidad de veces que aparecen las letras {letras} son: {cant_1}, {cant_2}, {cant_3} veces. \n"
)
# Cantidad de palabras
cant_palabras = len(texto.split())
print(f"El texto tiene un total de: {cant_palabras} palabras")

# Primer y ultima letra
primer_letra = texto[0]
ultima_letra = texto[-1]
print(
    f"La primer letra del texto es: {primer_letra} y la segunda letra del texto es: {ultima_letra}."
)

# Invertir y unir las palabras de la lista
reverso = texto.split()
reverso.reverse()
reverso = " ".join(reverso)
print(reverso)

# Esta la plabra pyhton?
busqueda = "python" in texto
dic = {True: "si", False: "no"}
print(f"Se encuentra la palabra python?: {dic[busqueda]}")
