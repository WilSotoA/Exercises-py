class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo una llamada : {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada {self.modelo}")


celular1 = Celular("Samsung", "S23", "49MP")
celular1 = Celular("Apple", "Iphone 15 pro", "80MP")

celular1.llamar()
