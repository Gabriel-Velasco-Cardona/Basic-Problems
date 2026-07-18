bruto = float(input("Ingrese su salario bruto ganado al mes: "))
#en este caso, usaré datos reales como retención del IMSS
#también usaré datos reales de retención de ISR
print("Retención del IMSS: 2.45%")
print("Retención del ISR: $505 fijos")
imss = bruto * 0.0245
isr = imss + 505
total = bruto - isr
print("El salario neto restante es del: " + str(total))
