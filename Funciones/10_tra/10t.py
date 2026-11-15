calif = []
Bon = []
for i in range(5):
    cal = float(input(f"Cuantas horas estudiaste en la materia {i+1}: "))
    calif.append(cal)

for j in calif:
    Bon.append(round(j * 2,2))
print(f"La siguiente semana estudiarás las siguientes cantidades de horas: {Bon}")


suma = sum(Bon)
valor_minimo = min(Bon)
valor_maximo = max(Bon)

print(f"Materia con menos horas a estudiar: {valor_minimo:.2f}")
print(f"Materia con mayor horas a estudiar: {valor_maximo:.2f}")
print(f"Total de horas a estudiar: {suma:.2f}")
