inicio = int(input("Escriba el primer número de la secuencia: "))
diferencia = int(input("Escriba la diferencia entre números de la secuencia: "))
limite = int(input("Escriba el limite de la secuencia: "))
num = inicio
while True: 
    print(num, end=" ")
    num += diferencia
    if num > limite: 
        break
print("\n Secuencia arítemica desde ",inicio, "Hasta", limite)
