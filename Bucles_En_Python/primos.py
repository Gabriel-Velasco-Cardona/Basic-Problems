N = int(input("Ingrese un número entero N mayor que 1: "))

if N <= 1:
    print("El número debe ser mayor que 1.")
else:
    contador_primos = 0
    print(f"\nNúmeros primos entre 2 y {N}:")
    
    for num in range(2, N + 1):
        es_primo = True

        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break  
        
        if es_primo:
            print(num, end=" ")
            contador_primos += 1
            
    print(f"\n\nTotal de primos encontrados: {contador_primos}")