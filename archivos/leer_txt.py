abrir_txt = open("archivos\\leer.txt", encoding="UTF-8")

# leer archivo completo
# archivo = abrir_txt.read()

# leer lina por linea
# lineas = abrir_txt.readlines()

# leer una sola linea
linea = abrir_txt.readline(10)

# cerrar el archivo
abrir_txt.close()

print(linea)
