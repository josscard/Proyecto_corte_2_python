from Vuelo import Vuelo
from Tiquete import Tiquete

class Aerolinea:
    def __init__(self):
        self.vuelos = []

    def crear_vuelo(self, origen, destino):
        vuelo = Vuelo(origen, destino)
        self.vuelos.append(vuelo)
        return vuelo

    def trayecto_mayor_recaudo(self):
        mayor = None
        monto = 0
        for v in self.vuelos:
            total = v.total_recaudo()
            if total > monto:
                mayor = v
                monto = total
        if mayor:
            return (mayor.origen, mayor.destino, monto)
        return None

    def quienes_viajan_mas(self, destino):
        hombres = 0
        mujeres = 0
        for v in self.vuelos:
            if v.destino == destino:
                for t in v.tiquetes:
                    if t.pasajero.genero == "masculino":
                        hombres += 1
                    elif t.pasajero.genero == "femenino":
                        mujeres += 1
        return "mujeres" if mujeres > hombres else "hombres"

    def costo_promedio_tiquete(self, origen, destino):
        total = 0
        cantidad = 0
        for v in self.vuelos:
            if v.origen == origen and v.destino == destino:
                for t in v.tiquetes:
                    total += t.valor_total
                    cantidad += 1
        return total / cantidad if cantidad > 0 else 0

    def recaudo_total_tiquetes(self):
        return sum([v.total_recaudo() for v in self.vuelos])

    def recaudo_total_equipaje(self):
        return sum([v.total_recaudo_equipaje() for v in self.vuelos])