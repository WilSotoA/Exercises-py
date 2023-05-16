with open("archivos\\leer.txt",'w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("insertando texto")
    
    #agregando dos lineas con writelines
    archivo.writelines(["-Que tal como estas","Buenas tardes \n"])
    archivo.writelines(["-todo bien","y tu"])