

from Pasajero import Pasajero  

class PasajeroEconomico(Pasajero):
    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 10)
        return exceso * 5000