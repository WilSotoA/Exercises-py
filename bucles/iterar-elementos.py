animales = ["gato","perro","loro","cocodrilo"]
numeros = [12,22,32,43]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora animal es: {animal}")
    
#recorriendo la lista numeros y multiplicando el valor por 10
for numero in numeros:
    print(numero*10)
    
#iterando dos listas del mismo tamaño al mismo tiempo con zip()
for animal,numero in zip(animales,numeros):
    print(f"recorriendo lista animales: {animal}")
    print(f"recorriendo lista numeros: {numero}")
    
#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando el for/ else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona de igual forma para tuplas