
#creando una lista (se pueden modificar)
lista = ["Wilmer Soto", True, 1.72]

#creando una tupla (no se pueden modificar)
tupla = ("Wilmer Soto", True, 1.72)

#esto es valido
lista[0] = "Wilmer"

#esto no es valido
#tupla[0] = "Wilmer"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Wilmer Soto", True, 1.72}

#creando un diccionario (dict) (la estructura es key : value separado con comas)
diccionario = {
    'nombre' : "Wilmer Soto",
    'estoy_emocionado' : True,
    'altura' : 1.72
}
print(diccionario['nombre'])