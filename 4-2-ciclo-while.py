while True:
    print('Luz')
    
    ##Valida Contraseña 
    contrasenia_correcta = "123456"
    intentos = 0
    
while False:
    contrasenia = input ("Ingrese por favor su contraseña: ")
    intentos += 1 
    if (contrasenia == contrasenia_correcta):
        print('contraseña correcta👌')
    else:
        print('contraseña incorrecta🥲')
    if(intentos >= 3):
         print('Tarjeta Bloqueada😒😒😒')
         
    break