peso = float(input("Ingresa tu masa corporal en Kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / altura**2
if(imc <= 24.9):
    print("Tu IMC es igual a: " + str(imc) + "Es un peso normal")
else:
    print("Tu IMC es igual a: "+ str(imc) + "Es sobrepeso")
