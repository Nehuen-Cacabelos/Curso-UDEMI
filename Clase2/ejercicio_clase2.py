nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
total_ventas = float(input("Ingrese el total de ventas realizadas: "))
sueldo_final = round(total_ventas * 0.13 + total_ventas, 2)

print(
    f"El sueldo final de {nombre} {apellido} con una comisión del 13% sobre un total de ventas de ${total_ventas} es de: ${sueldo_final}"
)
