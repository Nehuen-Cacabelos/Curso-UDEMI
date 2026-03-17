"""mascota = input("ingrese una mascota: ")

if mascota == "perro":
    print("tu mascota es un perro")
elif mascota == "gato":
    print("tu mascota es un gato")
else:
    print("no se que mascota tienes")

edad = 14
calificacion = 6

if edad <= 18:
    print("Eres menor de edad")
    if calificacion > 7:
        print("Tu calificacion esta aprobada")
    else:
        print("Has desaprobado")
else:
    print("Eres mayor de edad y ya no vas a la escuela")"""

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
    if num2 > num1:
        print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
