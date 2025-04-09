from CargaEspecial import CargaEspecial

class Bicicleta(CargaEspecial):
    def __init__(self, peso, tarifa_kilo):
        self.peso = peso
        self.tarifa_kilo = tarifa_kilo

    def calcular_costo(self, valor_tiquete):
        return self.peso * self.tarifa_kilo