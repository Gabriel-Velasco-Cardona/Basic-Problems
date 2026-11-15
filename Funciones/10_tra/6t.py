VectorInicial = []
VectorFinal = []
v = ["X","Y"]
for i in range(len(v)):
    pos = int(input(f"Ingresa la posición incial de {v[i]}: "))
    VectorInicial.append(pos)

for j in range(len(v)):
    add = int(input(f"Agrega la nueva posición para X y Y: ({v[j]}): "))
    VectorFinal.append(add)

suma = [a + b for a, b in zip(VectorInicial, VectorFinal)]
print(f"Nueva posición: {suma}")
