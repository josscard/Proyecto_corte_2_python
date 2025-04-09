class Pasajero:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.cargas_especiales = []

    def agregar_carga_especial(self, carga):
        self.cargas_especiales.append(carga)

    def obtener_descuento(self):
        return 0.07 if self.edad <= 13 else 0
