#creando diccionario con dict()
diccionario = dict(nombre="Wilmer",apellido="Soto")

#las listas no pueden ser claves y usamos frozenset para agregar conjuntos
diccionario = {frozenset(["wilmer","soto"]): "hola"}

#creando diccionario con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionario con fromkeys() con dos parametros
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)