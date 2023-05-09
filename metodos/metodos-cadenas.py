cadena1 = "Hola, soy Wilmer"

#convierte a mayuscula
mayus = cadena1.upper()

#convierte a minuscula
minus = cadena1.lower()

#primer letra en mayuscula
primer_letra_minuscula = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("a")

#si es numerico, devuelve true, sino false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devuelve true, sino false
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincide
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Hola");

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("Wilmer");

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 por el valor 2
cadena_nueva = cadena1.replace("Wilmer","Wilmer Andres");

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")

print(cadena_separada)