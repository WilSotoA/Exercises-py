#creando un conjunto con set()
conjunto = set(["Dato 1"])

#insertando un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato 1","dato 2"})
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificamos sí es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificamos sí es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verifica si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)