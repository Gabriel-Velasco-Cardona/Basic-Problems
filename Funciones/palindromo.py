def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""

    for caracter in texto: 
        if caracter != " ":
            limpio += caracter

    return limpio == limpio[::-1], limpio 

entrada = input("ingrese una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)

if resultado: 
    print("Es un palindromo")
else: 
    print("No es un palindromo")

print("La longuitud de la cadena limpia es: ", len(cadena_limpia))
