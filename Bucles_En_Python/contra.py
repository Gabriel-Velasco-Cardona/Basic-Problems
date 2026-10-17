contrasena_correcta = "123"
intentos = 0 
acceso = False

while intentos < 3 and not acceso:
    contrasena_usuario = input("Escriba la contraseña: ")
    intentos += 1
    
    if contrasena_usuario == contrasena_correcta:
        acceso = True 
    else: 
        print(f"Contraseña incorrecta. Te quedan {3 - intentos} intentos.")

if acceso: 
    print("Acceso autorizado")
else: 
    print("Incorrecto, bloqueado por 3 años")
    