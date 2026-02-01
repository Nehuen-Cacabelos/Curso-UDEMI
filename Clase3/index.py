mi_texto = "Esta es una prueba de string."

resultado = mi_texto[5]  # Accede al caracter en el indice 5
resultado = mi_texto[-1]  # Accede al ultimo caracter

resultado = mi_texto.index("e")  # Busca la primera "e"
resultado = mi_texto.index("e", 7)  # Busca la primera "e" despues del indice 7
resultado = mi_texto.index("e", 7, 16)  # Busca la primera "e" entre los indices 7 y 16

resultado = mi_texto.rindex("e")  # Busca la ultima "e"

print(resultado)
