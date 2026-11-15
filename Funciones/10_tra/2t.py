Tem = []
Semanas = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(Semanas)):
    temp = float(input(f"Proporciona la temperatura del día {Semanas[i]} ({i + 1}): "))
    Tem.append(temp)

total = sum(Tem)
valor_minimo = min(Tem)
valor_maximo = max(Tem)

print(f"Total de temperatura{total:.2f}")
print(f"Promedio: {total / len(Tem):.2f}")  
print(f"Valor mínimo: {valor_minimo:.2f}")
print(f"Valor máximo: {valor_maximo:.2f}")
