import abc
from abc import ABC

class Calefactor(ABC):
    __marca: str
    __modelo: str
    __paisfab: str
    __preciolista: float
    __metodopago: str
    __cuotas: int
    __promocion: bool

    def __init__(self, marca: str, modelo: str, paisfab: str, preciolista: float, metodo: str, cuotas: int, promo: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__paisfab = paisfab
        self.__preicolista = preciolista
        self.__metodopago = metodo
        if metodo.lower() == 'contado':
            self.__cuotas = 1
        else:
            self.__cuotas = cuotas
        if promo.lower() == 'si' and metodo == 'contado':
            self.__promocion = True
        else:
            self.__promocion = False
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_paisfab(self):
        return self.__paisfab
    
    def get_preciolista(self):
        return self.__preciolista
    
    def get_metodopago(self):
        return self.__metodopago
    
    def get_cuotas(self):
        return self.__cuotas
    
    def get_promocion(self):
        return self.__promocion
    
    @abc.abstractmethod
    def get_impventa(self):
        pass