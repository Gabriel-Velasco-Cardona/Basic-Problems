num = int(input("Ingresa un número entero: "))
if num == 0: 
    digitos = 1
else: 
    digitos = 0
    if num < 0:
        num = abs(num)
    while num > 0: 
        num //= 10
        digitos += 1
print("El número eledigo tiene: ", digitos, "Digitos")
