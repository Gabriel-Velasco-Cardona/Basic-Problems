consulta = input("Escriba la opción que le gustara recibir información: \n Inceptión \n Beatles \n Rick and Morty \n Stranger Things \n Avengers \n").lower()

match consulta: 
    case "inception":
        info = "Película de ciencia ficción dirigia por Christopher Nolan."
    case "beatles":
        info = "Banda británica de rock formada en 1960."
    case "rick and morty":
        info = "serie animada de comedia y ciencia ficción."
    case "tranger things":
        info = "serie de terror y ciencia ficción de Netflix."
    case "avengers": 
        info = "Película de superheroes del UMC."
    case _:
        info = "No se encontró nada."
print("Información de ",consulta, ": ",info)
