class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola 👋, estoy hablando un poco")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad} 👨‍🎨")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"Hola soy {self.nombre}, mi habilidad es: {self.habilidad} y trabajo en {self.empresa}"


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


figo = EmpleadoArtista("Figo", 31, "Paraguayo", "pintar", 1000000, "paint")

print(figo.presentarse())

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(figo, Persona)

print(instancia)

# roberto = Empleado("Roberto", 23, "Colombiano", "Programador", 100000)

# roberto.hablar()
