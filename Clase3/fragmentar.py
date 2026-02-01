abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = abecedario[2]  # Selecciona la letra en el índice 2
fragmento = abecedario[2:6]  # Selecciona las letras desde el índice 2 hasta el 5
fragmento = abecedario[:6]  # Selecciona las primeras 6 letras
fragmento = abecedario[20:]  # Selecciona las letras desde el índice 20 hasta el final
fragmento = abecedario[
    2:10:2
]  # Selecciona letras desde el índice 2 hasta el 9, saltando de 2 en 2

fragmento = abecedario[::-1]  # Invierte el string completo
fragmento = abecedario[::-2]  # Invierte el string, seleccionando de 2 en 2

print(fragmento)
