precios = []
Nombres = []

for i in range(4):
    Nombre = input(f"Proporciona el Nombre del producto {i + 1}: ")
    Nombres.append(Nombre)
    precio = float(input(f"Proporciona el precio del producto {i + 1}: "))
    precios.append(precio)

total = sum(precios)
valor_minimo = min(precios)
valor_maximo = max(precios)

print(f"Total: ${total:.2f}")
print(f"Valor mínimo: ${valor_minimo:.2f}")
print(f"Valor máximo: ${valor_maximo:.2f}")
print(f"Cosas compradas: {Nombres}")
