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

class PasajeroEconomico(Pasajero):
    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 10)
        return exceso * 5000
    
class PasajeroEjecutivo(Pasajero):
    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 20)
        return exceso * 10000
    
class PasajeroPremium(Pasajero):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.valor_tiquete = 0

    def calcular_exceso_equipaje(self, peso_maleta):
        exceso = max(0, peso_maleta - 30)
        return exceso * (self.valor_tiquete * 0.01)
