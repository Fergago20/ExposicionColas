from model.class1 import Cola
from model.class2 import Vuelo
class VueloDAO:
    def __init__(self):
        self.cola_vuelos = Cola()

    def agregar_vuelo(self, codigo, aerolinea, destino, tipo):
        if not self.verificar_vuelo(codigo):
            vuelo = Vuelo(codigo, aerolinea, destino, tipo)
            self.cola_vuelos.agregar(vuelo)
            return vuelo
        else:
            return None
        

    def quitar_vuelo(self):
        return self.cola_vuelos.quitar()

    def ver_primero(self):
        return self.cola_vuelos.ver_primero()

    def vacia(self):
        return self.cola_vuelos.vacia()

    def agregar_primero(self, codigo, aerolinea, destino, tipo):
        if self.verificar_vuelo(codigo):
            return None
        vuelo = Vuelo(codigo, aerolinea, destino, tipo)
        self.cola_vuelos.agregar_primero(vuelo)
        return vuelo

    def verificar_vuelo(self, codigo):
        for v in self.cola_vuelos.cola:
            if v.codigo == codigo:
                return True
        return False
    
    def todos(self):
        return self.cola_vuelos.todos()