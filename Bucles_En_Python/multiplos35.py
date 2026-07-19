print("Números divisibles por 3 y 5 desde el 1 hasta el 100: ")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()
