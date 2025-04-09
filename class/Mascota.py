from CargaEspecial import CargaEspecial

class Mascota(CargaEspecial):
    def __init__(self, tipo):
        self.tipo = tipo.lower()

    def calcular_costo(self, valor_tiquete):
        if self.tipo == "perro":
            return valor_tiquete * 0.05
        elif self.tipo == "gato":
            return valor_tiquete * 0.02
        return 0
