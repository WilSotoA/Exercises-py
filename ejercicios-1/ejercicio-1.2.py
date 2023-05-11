frase = input("escribe una frase, y calculo cuanto tardarias en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos")
if cantidad_de_palabras > 120:
    print("¡Mucho Texto!")
