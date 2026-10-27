total = 0
opcion = 0

print("--- MENÚ ---")
print("1) Hamburguesa - $80")
print("2) Pizza - $95")
print("3) Tacos - $60")
print("4) Terminar pedido")

while opcion != 4:
    opcion = int(input("Elige una opción (1-4): "))
    
    match opcion:
        case 1:
            total += 80
        case 2:
            total += 95
        case 3:
            total += 60
        case 4:
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")

if total > 300:
    total *= 0.85 
elif total > 150:
    total *= 0.95  

personas = int(input("¿Entre cuántas personas se divide la cuenta?: "))
pago_individual = total / personas

print("\n--- TOTALES POR PERSONA ---")
for i in range(1, personas + 1):
    print(f"Persona {i}: ${pago_individual:.2f}")
    