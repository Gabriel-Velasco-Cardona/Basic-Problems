meta = float(input("Cual es la meta de tu ahorro en pesos: "))
total = 0 
semanas = 0 

while total < meta: 
    semanas += 1
    ahorro = float(input(f"Cuanto ahorraste en la semana {semanas}: "))
    total += ahorro 
    print(f"LLevas ${total:.2f} de ${meta:.2f}")

print(f"\nMeta alcanzada en {semanas} semanas! Total ahorrado: ${total:.2f}")
