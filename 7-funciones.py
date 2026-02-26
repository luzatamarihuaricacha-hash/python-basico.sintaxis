#luz Atamari
#Funciones

print("hola, Juan")
print("bienvenido al sistema")
print("------------------------")

print("hola, Luz")
print("bienvenido al sistema")
print("------------------------")

print("hola, Pepito")
print("bienvenido al sistema")
print("------------------------")

print("-------------------------------------------")

nombres = ["Juan", "Luz", "Pepito"]
for i in nombres:
    print("Hola, ",i)
    print("bienvenido al sistema")
    print("---------------------------")

print("=============================================")

def saludar (nombre):
    print("Hola,",nombre)
    print("bienvenido al sistema")
    print("-------------------------------")

saludar("Juan")
saludar("Luz")
saludar("Pepito")

#Funciones con retorno (return)
def suma(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return(resultado)

print(suma(2,2))
 
print("--------------------------------------------")

#Funciones sin retorno
def suma2(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)

suma2(2,2)