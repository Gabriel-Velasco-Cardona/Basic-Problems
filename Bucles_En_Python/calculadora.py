while True: 
    print("1: Suma\n2: Resta\n3: Multiplicación\n4: División\n5: Salir")
    op = int(input("Cuál opción elige? "))
    if op == 5: 
        break 
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    match op:
        case 1: print(a+b)
        case 2: print(a-b)
        case 3: print(a*b)
        case 4: 
            if b != 0:
                print(a/b)
            else: 
                print("Error, división por cero")
    resp = input("¿Desea continuar? (s/n): ").lower()
    if resp == "n":
        break