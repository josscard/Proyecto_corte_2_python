from Pasajero import Pasajero  

class PasajeroEjecutivo(Pasajero):
    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 20)
        return exceso * 10000