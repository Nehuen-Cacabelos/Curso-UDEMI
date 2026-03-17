from random import *

aleatorio = randint(1, 100)
print(aleatorio)

aleatorio_decimal = uniform(1, 100)  # Genera un número decimal aleatorio entre 1 y 100
print(aleatorio_decimal)

aleatorio_decimal2 = random()  # Genera un número decimal aleatorio entre 0 y 1
print(aleatorio_decimal2)

string_aleatorio = ["azul", "rojo", "verde", "amarillo"]
print(choice(string_aleatorio))  # Elige un elemento aleatorio de la lista

cartas = ["pika", "charmander", "squirtle", "bulbasaur"]
shuffle(cartas)  # Mezcla la lista de cartas de forma aleatoria
print(cartas)
