while True:
    print("\n-- MENÚ DE OPCIONES --")
    print("1) Metros a centimetros")
    print("2) Kilometros a metros")
    print("3) Celcius a Fanhrenheit")
    print("4) Salir")
    
    opcion = int(input("Elige una opción (1-5): "))
    
    match opcion:
        case 1:
            C = int(input("Cuantas veces deseas repetir esto?:__"))
            for i in range(1,C+1):
                n = float(input("Ingrese la cantidad:__"))
                print(f"Esos metros se convierten en {n * 100} centimetros")
            
        case 2:
            C = int(input("Cuantas veces deseas repetir esto?:__"))
            for i in range(1,C+1):
                n = float(input("Ingrese la cantidad:__"))
                print(f"Esos kilometros se convierten en {n * 1000} metros")
            
        case 3:
            C = int(input("Cuantas veces deseas repetir esto?:__"))
            for i in range(1,C+1):
                n = float(input("Ingrese la cantidad:__"))
                print(f"Esos Celcius se convierten en {(n * 1.8)+32} grados Farhenheit")
            
        case 4:
            print("Bye Bye")
            break
            
        case _:
            print("Opción no válida. Intenta de nuevo.")
            