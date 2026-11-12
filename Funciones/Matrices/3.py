dinero = float(input("Ingrese la cantidad de dinero que posee actualmente: $"))
while dinero > 0:
    print("\n--MAQUINA EXPENDEDORA, ELIGA LO QUE DESEE--")
    print("1: Reresco ($15)")
    print("2: Papas Fritas ($12)")
    print("3: Galletas ($10)")
    print("4: Agua ($8)")

    Op = int(input("Ingrese la opción que desee:__"))

    match Op:
        case 1:
            precio = 15
            producto = "un refresco"
        case 2:
            precio = 12
            producto = "papas fritas"
        case 3:
            precio = 10
            producto = "galletas"
        case 4:
            precio = 8
            producto = "agua"
        case _:
            print("Opción inválida. Intente de nuevo.")
            continue 

    if dinero < precio:
        print("No te alcanza el dinero para este producto.")
    else:
            dinero = dinero - precio
            print(f"Ahora tienes {producto}")
            print(f"Cantidad actual: ${dinero}")
            for i in range(30):
                print("-", end="")

for i in range(30):
    print("-", end="")
print("Sin dinero") 

        