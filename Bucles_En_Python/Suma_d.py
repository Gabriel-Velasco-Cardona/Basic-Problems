numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("El número debe ser un entero positivo.")
else:
    numero_original = numero 
    suma = 0
    
    while numero > 0:
        digito = numero % 10  
        suma += digito        
        numero = numero // 10  
        
    print(f"La suma de los dígitos de {numero_original} es: {suma}")
        