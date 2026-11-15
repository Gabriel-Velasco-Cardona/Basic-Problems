Tem = []
Semanas = [1,2,3,4,5]

for i in range(len(Semanas)):
    temp = float(input(f"Proporciona la distancia recorrida del día {Semanas[i]}: "))
    Tem.append(temp)

total = sum(Tem)
valor_minimo = min(Tem)
valor_maximo = max(Tem)

print(f"Distancia total recorrida: {total:.2f}")
print(f"Distancia mínima: {valor_minimo:.2f}")
print(f"Distancia máxima: {valor_maximo:.2f}")
