#luz atamari
#tuplas Sets y Diccionarios

#Tuplas
# Simbolo ()
# por default lo ordena 
# inmutables = no se puede hacer cambios 
# te acepta duplicados 

tupla = (1, 2, 1, 2, 40, 10, 5, 11)
print(tupla)

#indices 
print(tupla[4])


#Sets
#simbolo {}
# No ordena
# Mutables = si puede hacer cambios 
# No te acepta duplicados 
sets = {1,2,3,1,2,3}
print(sets)

#add() agregar un nuevo dato
sets.add(4)
print(sets)

# remove() eliminar un dato
sets.remove(3)
print(sets)


# Diccionarios 
# Simbolos {key:value}
# Si ordena 

estudiante = {
    "nombre":"Luz",
    "natalidad" : "Puno",
    "edad" : 18,
    "carrera" : "Ingenieria"
}
print(estudiante)
print(estudiante["nombre"])
print(estudiante["natalidad"])
print(estudiante["edad"])
print(estudiante["carrera"])

estudiante["edad"] = 50
print(estudiante)

# Ciclo for en los diccionarios 
for clave,valor in estudiante.items():
    print("Clave: ", clave , "Valor: ", valor)
    
