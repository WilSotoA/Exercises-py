class Datos:
    def __init__(self):
        # con dos __ la propiedad es privada
        self.__password = "password"

    def _hablar(self):
        print("Hola, como estas")


datos = Datos()
print(datos._hablar())

# Getters and setters

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre


wilmer = Persona("Wilmer", 19)

print(wilmer.get_nombre())

wilmer.set_nombre("Andres")

print(wilmer.get_nombre())
