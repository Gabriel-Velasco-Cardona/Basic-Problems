Vel = []
Autos = ["McLaren MP4/4", "Porsche 917", "Audi Sport quattro", "Ford GT40", "Chevrolet NASCAR Gen 6"]

for i in range(len(Autos)):
    V = float(input(f"Proporciona la velocidad del auto: {Autos[i]} ({i + 1}): "))
    Vel.append(V)

total = sum(Vel)
valor_minimo = min(Vel)
valor_maximo = max(Vel)
Vma = Autos[Vel.index(valor_maximo)]
Vm = Autos[Vel.index(valor_minimo)]

print(f"Suma de las velocidades: {total:.2f}")
print(f"Promedio de las velocidades: {total / len(Vel):.2f}")  
print(f"Auto mas lento: {Vm} con una velocidad de {valor_minimo:.2f} KM")
print(f"Auto mas rápido: {Vma} con una velocidad de {valor_maximo:.2f} KM")
