#creando excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Comiste el siguiente error: {err}")

#lanzando mi propia funcion
#raise MiExcepcion("jajajaja estudia")

#manejando excepcion
try:
    raise MiExcepcion("jajajaja estudia")
except: 
    print("como vas a cometerlo")