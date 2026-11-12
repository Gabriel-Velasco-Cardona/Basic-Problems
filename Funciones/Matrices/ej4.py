precio = [53,28,72,67,69,25]
cantidad = []
producto = []
subtotal = []
for i in range(len(producto)):
    importe = precio[i] * cantidad[i]
    subtotal.append(importe)
    print(f"{cantidad[i]} x {producto[i:]}  ${importe:<8.2f}")

subtotal = sum(subtotal)
impuestos = subtotal * 0.16
total = subtotal + impuestos
