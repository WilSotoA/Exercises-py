import re

texto = """Hola amigo, esta es la cadena 1.
Esta es la 2 linea.
y Esta es la final."""

resultado = re.findall("Hola",texto)

#\d -> busca digitos numéricos del 0 - 9
resultado = re.findall(r"\d",texto)

#\D -> busca TODO menos digitos numéricos del 0 - 9
resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)

#\W -> busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios,tabs,saltos de linea
resultado = re.findall(r"\s",texto)

#\S -> busca TODO menos espacios en blanco -> espacios,tabs,saltos de linea
resultado = re.findall(r"\S",texto)

#. -> busca TODO menos saltos en linea
resultado = re.findall(r".",texto)

#\n -> busca saltos en linea
resultado = re.findall(r"\n",texto)

#\ -> cancela caracteres especiales
resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s",texto)

#^ -> busca el comienzo de una linea
#flags=re.M activa la multilinea
resultado = re.findall(r"^esta",texto,flags=re.M)

#$ -> busca el final de una linea
resultado = re.findall(r"final.$",texto,flags=re.M)

#{n} busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{3}",texto)

#{n,m} -> al menos n, como maximo m
resultado = re.findall(r"\d{1,4}",texto)

# | -> busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|Hola",texto)
print(resultado)
 