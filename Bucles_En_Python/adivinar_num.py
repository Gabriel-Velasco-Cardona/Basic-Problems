import random 
secreto = random.randint(1,100)
while True:
    intento = int(input("Adivina el numero, está entre el 1 y el 100: "))
    if intento < secreto: 
        print("Demasiado bajo!")
    elif intento > secreto: 
        print("Demasiado alto")
    else: 
        print("El numero es correcto! es: ",secreto)
        break

print("Juego terminado, el numero era: ",secreto)
