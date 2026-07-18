parcial = float(input("Ingrese nota del parcial (0-100)"))
proyecto = float(input("Ingrese nota del proyecto (0-100)"))
examen = float(input("Ingrese nota del examen (0-100)"))
if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
    print("Error: las notas deben estar entre 0 y 100")
else: 
    calificacion = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print("Calificación final: ", calificacion)
    