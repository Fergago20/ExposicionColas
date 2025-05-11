class Vuelo:
    def __init__(self, codigo, aerolinea, destino, tipo):
        self.codigo = codigo
        self.aerolinea = aerolinea
        self.destino = destino
        self.tipo = tipo

    def __str__(self):
        return f"Vuelo {self.codigo} de {self.aerolinea} a {self.destino} ({self.tipo})"
    