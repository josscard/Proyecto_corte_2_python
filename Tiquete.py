class Tiquete:
    def __init__(self, vuelo, pasajero, clase, valor_base):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.clase = clase
        self.valor_base = valor_base
        self.valor_total = self.calcular_valor_total()

    def calcular_valor_total(self):
        descuento = self.valor_base * self.pasajero.obtener_descuento()
        return self.valor_base - descuento
