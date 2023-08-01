class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")


nombre = input("Cual es tu nombre: ")
edad = input("Ahora tu edad: ")
grado = input("Por ultimo, tu grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(
    f"""
       DATOS DEL ESTUDIANTE \n
       Nombre: {estudiante.nombre}
       edad: {estudiante.edad}
       grado: {estudiante.grado}
       """
)
while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
