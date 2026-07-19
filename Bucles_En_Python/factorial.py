num = int(input("Ingrese el número para factorizar"))
factorial = 1
if num < 0:
    print("No es posible factorizar con numeros negativos")
else:
    for i in range(1, num + 1):
        factorial *= i 
print("El factorial de ",num, "es: ", factorial)