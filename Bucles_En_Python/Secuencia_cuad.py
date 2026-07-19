n = int(input("Número positivo: "))
i = 1
while True: 
    print(i ** 2)
    i += 1
    if i > n:
        break
print("Secuencia de cuadrados hasta: ",n)