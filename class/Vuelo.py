from Tiquete import Tiquete
from Pasajero import PasajeroEconomico, PasajeroEjecutivo, PasajeroPremium

class Vuelo:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.tiquetes = []

    def vender_tiquete(self, pasajero, clase, valor_base):
        if clase == "economica":
            pasajero = PasajeroEconomico(pasajero.nombre, pasajero.edad, pasajero.genero)
        elif clase == "ejecutiva":
            pasajero = PasajeroEjecutivo(pasajero.nombre, pasajero.edad, pasajero.genero)
        elif clase == "premium":
            pasajero = PasajeroPremium(pasajero.nombre, pasajero.edad, pasajero.genero)
            pasajero.valor_tiquete = valor_base
        else:
            raise ValueError("Clase inválida")
        tiquete = Tiquete(self, pasajero, clase, valor_base)
        self.tiquetes.append(tiquete)
        return tiquete

    def devolver_tiquete(self, tiquete):
        if tiquete in self.tiquetes:
            self.tiquetes.remove(tiquete)

    def check_in(self, tiquete, peso_maleta):
        costo_exceso = tiquete.pasajero.calcular_exceso_equipaje(peso_maleta)
        costo_carga = sum([carga.calcular_costo(tiquete.valor_total) for carga in tiquete.pasajero.cargas_especiales])
        return costo_exceso + costo_carga

    def total_recaudo(self):
        return sum([t.valor_total for t in self.tiquetes])

    def total_recaudo_equipaje(self):
        total = 0
        for t in self.tiquetes:
            total += t.pasajero.calcular_exceso_equipaje(0)
            total += sum([carga.calcular_costo(t.valor_total) for carga in t.pasajero.cargas_especiales])
        return total