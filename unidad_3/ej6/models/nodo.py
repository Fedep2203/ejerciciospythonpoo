class Nodo:
    __dato: object
    __siguiente: object

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def set_siguiente(self, dato):
        self.__siguiente = dato
    
    def get_dato(self):
        return self.__dato
    
    def get_siguiente(self):
        return self.__siguiente