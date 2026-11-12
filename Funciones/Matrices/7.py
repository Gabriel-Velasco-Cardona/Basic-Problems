u_puntos, pc_puntos = 0, 0

for r in range(1, 6):
    pc = "piedra" if r % 2 != 0 else "papel"
    
    user = input(f"\nRonda {r} - Elige (piedra/papel/tijera): ").lower().strip()
    while user not in ["piedra", "papel", "tijera"]:
        user = input("Opción inválida. Intenta de nuevo: ").lower().strip()
        
    match user:
        case "piedra" | "papel" | "tijera":
            pass

    print(f"La computadora eligió: {pc}")

    if user == pc:
        print("Empate en esta ronda.")
    elif (user == "piedra" and pc == "tijera") or \
         (user == "papel" and pc == "piedra") or \
         (user == "tijera" and pc == "papel"):
        print("¡Ganaste esta ronda!")
        u_puntos += 1
    else:
        print("Gana la computadora esta ronda.")
        pc_puntos += 1

print(f"\n--- PUNTOS FINALES ---")
print(f"Tú: {u_puntos} | Computadora: {pc_puntos}")

if u_puntos > pc_puntos:
    print("¡Felicidades, ganaste el juego!")
elif pc_puntos > u_puntos:
    print("La computadora ganó el juego.")
else:
    print("El juego terminó en empate.")
    