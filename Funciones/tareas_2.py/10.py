aciertos = 0
print("EXAMEN")

for i in range(1, 5):
    
    match i:
        case 1:
            pregunta = "¿Cuál es la capital de Francia?\na) Londres\nb) París\nc) Berlín"
            correcta = "b"
        case 2:
            pregunta = "¿Cuánto es 2 + 2?\na) 4\nb) 5\nc) 3"
            correcta = "a"
        case 3:
            pregunta = "¿Qué lenguaje de programación se está usando aquí?\na) Java\nb) C++\nc) Python"
            correcta = "c"
        case 4:
            pregunta = "¿Cuál es el planeta rojo?\na) Marte\nb) Venus\nc) Júpiter"
            correcta = "a"

    print(f"\nPregunta {i}:")
    print(pregunta)
    respuesta = input("Elige una opción (a, b, c): ").lower().strip()
    while respuesta not in ["a", "b", "c"]:
        respuesta = input("Opción no válida. Ingresa a, b o c: ").lower().strip()
    if respuesta == correcta:
        print("¡Correcto!")
        aciertos += 1
    else:
        print(f"Incorrecto. La respuesta correcta era la '{correcta}'.")
print(f"Tus aciertos totales: {aciertos} de 4")

if aciertos == 4:
    print("Resultado: Excelente")
elif aciertos == 3:
    print("Resultado: Bien")
elif aciertos == 2:
    print("Resultado: Regular")
else:
    print("Baboso")