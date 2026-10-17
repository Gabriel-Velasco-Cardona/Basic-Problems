edad = int(input("Ingrese su edad: "))

while edad < 1 or edad > 120:
    print("Error: La edad debe estar entre 1 y 120 años. Intente nuevamente.")
    edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"Usted tiene {edad} años. Es mayor de edad.")
else:
    print(f"Usted tiene {edad} años. Es menor de edad.")