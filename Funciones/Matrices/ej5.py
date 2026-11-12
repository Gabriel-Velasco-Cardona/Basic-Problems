precio = [34,50,20,12,99]
producto = []
cantidad = []
importe = []
subtotales = []

for i in range(len(precio)):
    npu = input(f"Proporciona el nombre del producto {i+1}: ")
    producto.append(i)
for a in range(len(precio)):
    cant = int(input(f"Cantidad de {producto[a]} a comprar"))
    cantidad.append(cant)

for j in range(len(producto)):
    importe = precio[j] * cantidad[j]
    subtotales.append(importe)
    print(f"{producto[j]} x {cantidad[j]} = ${importe:.2f}")

subtotal = sum(subtotales)
impuesto = subtotal * 0.16
total = subtotal + impuesto

print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA: ${impuesto:.2f}")
print(f"Total a pagar ${total:.2f}")

pos = subtotales.index(max(subtotales))
print(f"Mayor gasto: {producto[pos]} (${subtotales[pos]:.2f})")
