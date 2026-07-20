def maximo_manual(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo: 
            maximo = num 
    return maximo 

def minimo_manual(lista):
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista: 
        if num < minimo:
            minimo = num
    return minimo 

numeros = []
for i in range(8):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

mayor_manual = maximo_manual(numeros)
menor_manual = minimo_manual(numeros)

print("Mayor (manual): ",mayor_manual)
print("Menor (manual: ): ",menor_manual)
