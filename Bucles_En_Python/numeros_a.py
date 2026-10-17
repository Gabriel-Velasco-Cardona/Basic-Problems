palabra = input("Ingrese una frase: ")
contador = 0

for letra in palabra.lower(): 
    if letra in "aeiou":
        contador += 1

print("Las vocales aparecen un total de", contador, "veces")
