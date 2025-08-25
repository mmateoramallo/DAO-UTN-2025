class Surtidor:
    def __init__(self, numero_surtidor, cantidad, tipo):
        self.numero_surtidor = numero_surtidor
        self.cantidad = cantidad
        self.tipo = tipo

    def __str__(self):
        return f"Surtidor {self.numero_surtidor}: {self.cantidad} litros de tipo {self.tipo}"
    
    