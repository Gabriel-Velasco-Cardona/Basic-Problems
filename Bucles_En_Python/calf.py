cantidad = int(input("Cantidad"))
suma = 0 
for i in range(1,cantidad+1):
    califacion = float(input(f"Cali {i}"))
    suma += califacion + suma 
    promedio = suma / cantidad
    print(f"promedio es: {promedio}")