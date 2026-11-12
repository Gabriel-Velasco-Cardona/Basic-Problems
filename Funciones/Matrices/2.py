while True:
    print("\n-- MENÚ DE OPERACIONES --")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    match opcion:
        case "1":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado de la suma: {n1 + n2}")
            
        case "2":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado de la resta: {n1 - n2}")
            
        case "3":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado de la multiplicación: {n1 * n2}")
            
        case "4":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            if n2 == 0:
                print("No se puede dividir entre cero")
            else:
                print(f"Resultado de la división: {n1 / n2}")
                
        case "5":
            print("Bye Bye")
            break
            
        case _:
            print("Opción no válida. Intenta de nuevo.")

    for _ in range(30):
        print("-", end="")