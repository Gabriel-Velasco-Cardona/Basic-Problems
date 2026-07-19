while True: 
    letra = input("Ingrese letra (espacio termina): ")
    if letra == " ":
        break
    letra = letra.lower()
    if letra in "aeiou":
        print("Es una Vocal")
    else:
        print("Consonante")
print("Progama Finalizado")
