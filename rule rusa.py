import random

# Crear una ruleta con 6 posiciones y una bala en una posición aleatoria
bala = random.randint(1, 6)

print("=== Juego de Ruleta Rusa ===")
print("Ingresa un número del 1 al 6. Si aciertas donde está la bala... pierdes.")

while True:
    try:
        numero = int(input("Elige una cámara (1-6): "))
        
        if numero < 1 or numero > 6:
            print("Por favor, ingresa un número válido entre 1 y 6.")
            continue

        if numero == bala:
            print("💥 ¡Perdiste! La bala estaba en esa cámara.")
            break
        else:
            print("😅 Te salvaste... intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número.")
6