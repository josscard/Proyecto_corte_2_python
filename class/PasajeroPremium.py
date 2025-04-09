from Pasajero import Pasajero

class PasajeroPremium(Pasajero):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.valor_tiquete = 0

    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 30)
        return exceso * (self.valor_tiquete * 0.01)