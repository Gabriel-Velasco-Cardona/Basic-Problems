Tem = []
Semanas = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(Semanas)):
    temp = float(input(f"Proporciona el gasto realizado del día {Semanas[i]} ({i + 1}): "))
    Tem.append(temp)

total = sum(Tem)
valor_minimo = min(Tem)
valor_maximo = max(Tem)
diaM = Semanas[Tem.index(valor_maximo)]
diam = Semanas[Tem.index(valor_minimo)]

print(f"Total acumulado: ${total:.2f}") 
print(f"Día de gasto menor: {diam} con un {valor_minimo} de gasto")
print(f"Día de mayor gasto: {diaM} con un {valor_maximo} de gasto")
