with open("archivos\\leer.txt",'a',encoding="UTF-8") as archivo:
    archivo.write("\n")
    #agregando el archivo
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada \n")