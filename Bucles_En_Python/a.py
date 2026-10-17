C = int(input("Ingrese la cantidad a calcular: "))
S = 0

for i in range(C):
    Ca = float(input(f"Introduzca calificación {i + 1}: "))
    S += Ca

promedio = S / C
print(f"el promedio es: {promedio: .2f}")

if promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")
