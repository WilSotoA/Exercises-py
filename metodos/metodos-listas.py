#creando una lista con list()
lista = list([19])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(4)

#agregando un elemento a la lista en un indice especifico
lista.insert(0,22)

#agregando varios elementos a la lista
lista.extend([False, 2023])

#eliminando un elemento de la lista (por su indice)
lista.pop(0) #-1 para eliminar el ultimo

#removiendo un elemento de la lista por su valor
lista.remove(19)

#eliminando todos los elementos de la lista 
#lista.clear()

#ordenando la lista ascendente(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(False);

print(elemento_encontrado)