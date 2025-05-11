from collections import deque
class Cola:
    def __init__(self):
        self.cola = deque()
    def agregar(self, elemento):
        self.cola.append(elemento)

    def quitar(self):
        if len(self.cola) > 0:
            return self.cola.popleft()
        else:
            return None
        
    def vacia(self):
        return len(self.cola) == 0
    
    
    def ver_primero(self):
        if len(self.cola) > 0:
            return self.cola[0]
        else:
            return None
        
    def agregar_primero(self, elemento):
        self.cola.appendleft(elemento)

    def todos(self):
        return self.cola.copy()