import math

def mcd(a,b):
    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0: 
        return 0 
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)

print(f"MCD cálculado: {resultado}")
print(f"MCD con match.gcd: {resultado_math}")
print("Los resultados "+ ("si " if resultado == resultado_math else "no ") + "coinciden")

if num1 == 0 and num2 == 0: 
    print("Caso especial: ambos números son cero")
else: 
    print("Programada terminado")