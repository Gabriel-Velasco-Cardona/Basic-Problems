n = int(input("Ingresa un numero positivo: "))
i = 1
while True:
    if i % 2 != 0:
        print(i, end="-")
    i += 1
    if i > n:
        break
print("\n Fin. Se mostraron los impares hasta ",n)