while True: 
    print("Instrucciones: ingrese un numero del 1 al 7")
    opcion = int(input("INGRESAR AQUÍ: "))

    match opcion: 
        case 1: 
            print("Hoy es Domingo") 
            print("Por ende, no tiene clases, disfrute")
        case 2:    
            print("Hoy es Lunes, padre santo")
            materias = int(input("Ingrese cuantas materias tiene el día de hoy__ "))
            for i in range(1, materias +1):
                n = input(f"Ingrese el nombre de la materia {i}:__ ")
                print(f"Materia {i}:__ {n}")
        case 3: 
            print("Hoy es Martes, santa madre")
            materias = int(input("Ingrese cuantas materias tiene el día de hoy__ "))   
            for i in range(1, materias +1):
                n = input(f"Ingrese el nombre de la materia {i}:__ ")
                print(f"Materia {i}:__ {n}")
        case 4:    
            print("Hoy es Miercoles, Madre mia")
            materias = int(input("Ingrese cuantas materias tiene el día de hoy__ "))
            for i in range(1, materias +1):
                n = input(f"Ingrese el nombre de la materia {i}:__ ")
                print(f"Materia {i}:__ {n}")
        case 5:    
            print("Hoy es Jueves, Santo dios")
            materias = int(input("Ingrese cuantas materias tiene el día de hoy__ "))
            for i in range(1, materias +1):
                n = input(f"Ingrese el nombre de la materia {i}:__ ")
                print(f"Materia {i}:__ {n}")
        case 6:    
            print("Hoy es Viernes, Dios mio sálvame")
            materias = int(input("Ingrese cuantas materias tiene el día de hoy__ "))
            for i in range(1, materias +1):
                n = input(f"Ingrese el nombre de la materia {i}:__ ")
                print(f"Materia {i}:__ {n}")
        case 7:    
            print("Hoy es Sabado, Lets goooo")
            print("Hoy no tienes clases")
        case _:
            print("Opción no válida")
