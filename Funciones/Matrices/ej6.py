alumnos = []
calificaciones = []
aprobados = []
reprobados = []
alu = int(input("Cantidad de alumnos__"))
for i in range(alu):
    nombre = input(f"Proprocione el nombre del alumno: {i+1}__")
    alumnos.append(nombre)
    calif = float(input(f"Dame la calificación del alumno: {alumnos[i]} __"))
    calificaciones.append(calif)
    if calificaciones[i] >= 7:
        aprobados.append(alumnos[i])
    else:
        reprobados.append(alumnos[i])

promedio = sum(calificaciones)
print(f"Promedio: {promedio / alu:.2f}")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")