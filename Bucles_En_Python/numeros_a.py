palabra = input("Ingrese una palabra que contenga a: ").lower()
contador = 0
for letra in palabra: 
    if letra == "a":
        contador +=1
print("La letra a aparece ",contador," veces")
