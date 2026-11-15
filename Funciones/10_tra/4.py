calif = []
Bon = []
for i in range(5):
    cal = float(input(f"Ingrese la calificación {i+1}: "))
    calif.append(cal)

for j in calif:
    Bon.append(round(j * 1.1,2))
print(f"resultado alterados: {Bon}")
suma = sum(Bon)
print(f"Suma de las calificaciones anteriores: {suma:.2f}")
