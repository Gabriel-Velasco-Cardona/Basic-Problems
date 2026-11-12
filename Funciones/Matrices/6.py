total = int(input("¿Cuántos alumnos hay?: "))
presentes = 0
faltas = 0
retardos = 0

for i in range(1, total + 1):
    letra = input(f"Alumno {i} (P/F/R): ").upper()
    
    while letra not in ["P", "F", "R"]:
        letra = input("Opción no válida. Ingrese P, F o R: ").upper()
    
    match letra:
        case "P":
            presentes += 1
        case "F":
            faltas += 1
        case "R":
            retardos += 1

if faltas == 0:
    asistencia = "Excelente"
elif faltas <= 3:
    asistencia = "Regular"
else:
    asistencia = "Deficiente"

print(f"\nPresentes: {presentes} | Faltas: {faltas} | Retardos: {retardos}")
print(f"Asistencia del grupo: {asistencia}")
