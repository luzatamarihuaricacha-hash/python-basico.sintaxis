#luz atamari
#listas 
lista = ['Luz','Atamari',25,True]
print(lista[0])
# lista de futas.
frutas = ['Fresa','Mango','Pera','Manzana','Sandia']
print(frutas[3])

frutas[1] = 'Uva'
print(frutas) 

# Matriz 
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[2][2])

#lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])
#Ciclo for en la listas 
for i in numeros:
    print(i *10)
for i in frutas:
    print(i)

# Metdos en las listas 
print("---------------------Metodos")
frutas = ['Fresa','Mango','Pera','Manzana','Sandia']

#Aagragar un nuevo dato
frutas.append("Ciruela")
print(frutas)
# Insert = insertar un dato
frutas.insert(2,"Platano")
print(frutas)

# Remove = borrar un dato
frutas.remove("Mango")
print(frutas)

# pop = para obtener o eliminar el ultimo dato
frutas.pop()
print(frutas)

# sort() = ordenar la lista 
frutas.sort()
print(frutas)

# reverse = revertir 
frutas.reverse()
print(frutas)

#len() = contar datos
cantidad = len(frutas)
print(cantidad)

#Index() = encontrar el indice
indice = frutas.index("Manzana")
print(indice)
