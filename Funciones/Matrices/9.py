while True: 

    print("\n MENU DE FIGURAS")
    print("1: Cuadrado")
    print("2: Triangulo")
    print("3: Linea")
    print("4: salir")
    Op = int(input("Selecciona una opción:__"))

    match Op:
        case 1:
            T = int(input("Ingrese el tamaño de la figura:__"))
            
            for i in range(T):
                for j in range(T):
                    print("*", end="")
                print()
                
        case 2:
            T = int(input("Ingrese el tamaño de la figura:__"))

            for i in range(1, T + 1):
                for j in range(i):
                      print("*", end="")

                print()
                
        case 3:
            T = int(input("Ingrese el tamaño de la figura:__"))
            
            for i in range(1, T + 1):
                 print("*", end="")
            print()
                
        case 4:
            print("Bye Bye")
            break
                
        case _:
                print("Opción no válida. Intenta de nuevo.")