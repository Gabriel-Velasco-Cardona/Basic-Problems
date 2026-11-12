C = int(input("Cuantos meses quiere consultar?__"))
for i in range(1, C+1):
    Op = int(input("Ingrese un numero del 1 al 12__"))
    while True: 
        match Op: 
            case 12 | 1 | 2: 
                if Op == 12: 
                    print("Es Diciembre")
                elif Op == 1: 
                    print("Es Enero")
                elif Op == 2:
                    print("Es Febrero")
                print("Es Invierno")
                break
            case 3 | 4 | 5: 
                if Op == 3:
                    print("Es Marzo")
                elif Op == 4: 
                    print("Es Abril")
                elif Op == 5: 
                    print("Es Mayo")
                print("Es primavera")
                break
            case 6 | 7 | 8:
                if Op == 6: 
                    print("Es Junio")
                elif Op == 7:
                    print("Es Julio")
                elif Op == 8: 
                    print("Es Agosto")
                print("es verano")
                break
            case 9 | 10 | 11:
                if Op == 9: 
                    print("Es Septiembre")
                elif Op == 10: 
                    print("Es Octubre")
                elif Op == 11:
                    print("Es Noviembre")
                print("Es Otoño")
                break
            case _: 
                print("numero no válido")
                break
