suma = 0
contador = 0
while True:
    num = float(input("Ingresa un número positivo (si ingresa un negativo, sale): "))
    if num < 0:
        break
    if num > 0: 
        suma += num 
        contador += 1
if contador > 0: 
    media = suma / contador
    print("La medía de todos los numeros ingresados es: ", media)
else: 
    print("No se ingresaron positivos")