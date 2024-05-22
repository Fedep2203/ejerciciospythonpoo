import abc
from abc import ABC

class Publicacion(ABC):
    __titulo: str
    __categoria: str
    __preciobase: float

    def __init__(self, titulo, categoria, preciobase):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__preciobase = preciobase
    
    def get_titulo(self):
        return self.__titulo
    
    def get_categoria(self):
        return self.__titulo
    
    def get_preciobase(self):
        return self.__preciobase
    
    @abc.abstractmethod
    def get_impventa(self):
        pass