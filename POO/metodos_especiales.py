class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"

    def __repr__(self):
        return f'Persona("{self.nombre}","{self.edad}")'

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)


wilmer = Persona("Wilmer", 19)
andres = Persona("Pedro", 30)
maria = Persona("Pedro", 20)

nueva_persona = wilmer + andres + maria

print(nueva_persona.edad)

# repre = repr(wilmer)
# resultado = eval(repre)

# print(resultado.nombre)
