serie = "NH-60"

match serie:
    case "NH-50":
        print("La serie es NH-50")
    case "NH-90":
        print("La serie es NH-90")
    case _:
        print("La serie no es NH-50 ni NH-90")

pelicula = {"titulo": "El Padrino", "director": "Francis Ford Coppola", "anio": 1972}
cine = {
    "nombre": "Cinepolis",
    "peliculas": {"Los Vengadores": 2012, "Los Simpson": 2007, "Titanic": 1997},
}

lista_peliculas = [pelicula, cine, "algo"]

for e in lista_peliculas:
    match e:
        case {"titulo": titulo, "director": director, "anio": anio}:
            print(
                f"La película es {titulo}, dirigida por {director} y estrenada en {anio}."
            )
        case {"nombre": nombre, "peliculas": peliculas}:
            print(
                f"El cine se llama {nombre} y tiene las siguientes películas: {peliculas}."
            )
        case _:
            print("No se reconoce el formato de la película o cine.")
