n = int(input("Cantidad de números a ingresar: "))
mayores = 0
menores = 0 
iguales = 0 
for i in range(n):
    num = int(input("Número: "))
    if num > 0:
        mayores +=1
    elif num < 0: 
        menores +=1
    else: 
        iguales += 1
print("Mayores a 0: ",mayores)
print("Menores a 0: ",menores)
print("Iguales a 0: ",iguales)
