celcius = float(input("Ingrese la temperatura en celcius: "))
print("Eliga una opción \n 1: Fahrenheit \n 2: Kelvin")
opcion = int(input("Elige una opción: "))
match opcion: 
    case 1: 
        resultado = celcius * 9/5 + 32
        unidad = "°f"
    case 2:
        resultado = celcius + 273.15
        unidad = "°K"
    case _: 
        resultado = None
        print("Opción Invalida")
if resultado is not None:
    print(f"Convertido: {resultado} {unidad}")
    