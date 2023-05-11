frutas = ["banana","manzana","pera","mango","naranja","guayaba"]
cadena = "Hola Dalto"
numeros = [2,5,8,10]
#saltando una iteracion con una guayaba con la sentencia continue
for fruta in frutas:
    if fruta == "guayaba":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"me voy a comer una {fruta}")
else:
    print("terminado")

#recorrer cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)