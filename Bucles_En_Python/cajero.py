saldo = 1000
opcion = 0

while opcion != 4:
    print("\nMENÚ DE CAJERO AUTOMÁTICO")
    print("1) Consultar saldo")
    print("2) Depositar")
    print("3) Retirar")
    print("4) Salir")
    
    opcion = int(input("Elija una opción (1-4): "))
    
    if opcion == 1:
        print(f"\nSu saldo actual es: ${saldo:.2f}")
        
    elif opcion == 2:
        deposito = float(input("\nIngrese la cantidad a depositar: $"))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
        else:
            print("Error: No se pueden depositar cantidades negativas o iguales a cero.")
            
    elif opcion == 3:
        retiro = float(input("\nIngrese la cantidad a retirar: $"))
        if retiro <= 0:
            print("Error: La cantidad a retirar debe ser mayor a cero.")
        elif retiro > saldo:
            print(f"Error: Fondos insuficientes. Su saldo actual es de ${saldo:.2f}")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
            
    elif opcion == 4:
        print("\nGracias por usar nuestro cajero. ¡Hasta luego!")
        
    else:
        print("\nOpción inválida. Por favor, elija un número entre 1 y 4.")