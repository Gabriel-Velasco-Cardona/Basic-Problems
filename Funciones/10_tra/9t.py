Linea = []
Tienda = []
Comp = []
Producto = [1,2,3,4]
for i in range(len(Producto)):
    preL = int(input(f"Ingresa el valor del prodcuto {Producto[i]} en la tienda en línea: "))
    Linea.append(preL)
    preF = int(input(f"Ingresa el valor del prodcuto {Producto[i]} en la tienda física: "))
    Tienda.append(preF)

Comp = [l < t for l, t in zip(Linea, Tienda)]
suma_precios = [l + t for l, t in zip(Linea, Tienda)]

print(f"Vector Comp (¿Más barato en línea?): {Comp}")
print(f"Suma de ambas listas: {suma_precios}")
