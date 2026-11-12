filas, columnas = 3,4
m = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(0)
    m.append(fila)

for i in range(filas):
    for j in range(columnas):
        m[i][j] = int(input(f"[{i}] [{j}]: "))

for i in m:
    print(i)
        
            