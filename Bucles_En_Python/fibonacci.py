limite = int(input("Escribe el numero limite de la serie"))
a,b= 0,1
while a <= limite: 
    print(a, end=" ")
    a,b=b, a+b
    print()