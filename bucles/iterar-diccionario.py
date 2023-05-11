diccionario = {
    "nombre": "Wilmer",
    "apellido": "Soto",
    "edad": 19,
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f"la clave es: {key}")

#recorriendo diccionario con items() para obtener las claves y el valor
for item in diccionario.items():
    key = item[0]
    value = item[1]
    print(f"la clave es: {key} y el valor es: {value}")