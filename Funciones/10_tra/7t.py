Ventas = []
Semanas = [1,2,3,4]

for i in range(len(Semanas)):
    V = float(input(f"Proporciona las utilidades de la semana {Semanas[i]}: "))
    Ventas.append(V)

total = sum(Ventas)
valor_minimo = min(Ventas)
valor_maximo = max(Ventas)
diaM = Semanas[Ventas.index(valor_maximo)]
diam = Semanas[Ventas.index(valor_minimo)]

print(f"Total acumulado: ${total:.2f}") 
print(f"Día de gasto menor: {diam} con un {valor_minimo} de gasto")
print(f"Día de mayor gasto: {diaM} con un {valor_maximo} de gasto")
