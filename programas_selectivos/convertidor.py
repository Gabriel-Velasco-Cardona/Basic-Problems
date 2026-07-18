cantidad = float(input("Ingrese su capital en pesos mexicanos: "))
print("Moendas disposinles: \n 1: Dólas \n 2: Euro \n 3: Bath \n 4: Yen \n 5: won \n 6: Dólar austriaco \n 7: Sol \n 8: Dólas canadiense \n 9: Bolívar \n 10: peso argentino")
opcion = int(input("Elige una opción: "))
match opcion: 
    case 1:
        resultado = cantidad / 16.5
        moneda = "USD"  
    case 2:
        resultado = cantidad / 18
        moneda = "EUR"
        resul = round(resultado,2)
    case 3:
        resultado = cantidad / 0.45
        moneda = "THB"
        resul = round(resultado,2)
    case 4:
        resultado = cantidad / 0.12
        moneda = "JPY"
        resul = round(resultado,2)
    case 5:
        resultado = cantidad / 0.013
        moneda = "KRW"
        resul = round(resultado,2)
    case 6:
        resultado = cantidad / 11.5
        moneda = "AUD"
        resul = round(resultado,2)
    case 7:
        resultado = cantidad / 2.8
        moneda = "PEN"
        resul = round(resultado,2)
    case 8:
        resultado = cantidad / 8.2
        moneda = "CAD"
        resul = round(resultado,2)
    case 9:
        resultado = cantidad / 0.0023
        moneda = "VES"            
        resul = round(resultado,2)   
    case 10:
        resultado = cantidad / 0.046        
        moneda = "ARS"   
        resul = round(resultado,2)
    case _:
        print("Opción no valida")
        resultado = None
print("los ",cantidad, "se trasforman en: ",resul, moneda)