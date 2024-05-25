from zope.interface import implementer
from models.nodo import Nodo
from interfaces.ILista import ILista

@implementer(ILista)
class Lista:
    __cabeza: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        self.__actual = self.__cabeza
        self.__indice = 0
        return self
    
    def tojson(self):
        diccionario = {
            '__class__': self.__class__.__name__,
            'calefactores': [calefactores.tojson() for calefactores in self]
        }
        return diccionario

    def __next__(self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__cabeza
            raise StopIteration
        else:
            self.__indice +=1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
    
    def insertar_inic(self, dato: object):
        nodo = Nodo(dato)
        nodo.set_siguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertar_enpos(self, pos: int, dato: object):
        aux = self.__cabeza
        if aux == None or pos == 1:
            nodo = Nodo(dato)
            nodo.set_siguiente(self.__cabeza)
            self.__cabeza = nodo
            self.__tope += 1
        elif 0 < pos <= self.__tope:
            anterior = None
            siguiente = None
            i = 0
            nodo = Nodo(dato)
            while aux != None and i < pos:
                anterior= aux
                aux = aux.get_siguiente()
                i += 1
            anterior.set_siguiente(nodo)
            nodo.set_siguiente(aux)
            self.__tope += 1
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')       
    
    def mostrar_datoesp(self, pos: int):
        print('<------------------------------------------------------------------------------------->')
        if 0 < pos <= self.__tope:
            aux = self.__cabeza
            if aux == None:
                print('La lista se encuentra vacia')
            else:
                i = 0
                while aux != None and i < pos:
                    anterior = aux
                    aux = aux.get_siguiente()
                    i += 1
                if anterior == None:
                    print('El elemento no existe.')
                else:
                    print(anterior.get_dato())
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')

    def insertar_final(self, dato: object):
        aux = self.__cabeza
        if aux == None:
            nodo = Nodo(dato)
            nodo.set_siguiente(aux)
            self.__cabeza = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            anterior = None
            while aux != None:
                anterior = aux
                aux = aux.get_siguiente()
            nodo = Nodo(dato)
            nodo.set_siguiente(aux)
            anterior.set_siguiente(nodo)
            self.__tope += 1
    
    def menor_precio_gas(self):
        from models.calefactor_gas import CalefactorGas
        print('<------------------------------------------------------------------------------------->')
        minprice = 999999999.9
        dato = None
        for calefactor in self:
            if isinstance(calefactor, CalefactorGas):
                if calefactor.get_preciolista() < minprice:
                    minprice = calefactor.get_preciolista()
                    dato = calefactor
        print(dato)

    def mostrar_modelos_elec(self, marca: str):
        from models.calefactor_elec import CalefactorElec
        print('<------------------------------------------------------------------------------------->')
        for calefactor in self:
            if isinstance(calefactor, CalefactorElec):
                if calefactor.get_marca() == marca:
                    print(f'Modelo: {calefactor.get_modelo()}\nPotencia: {calefactor.get_potencia()}\nPrecio de Lista: {calefactor.get_preciolista()}')
    
    def mostrar_datospromo(self):
        print('<------------------------------------------------------------------------------------->')
        for calefactor in self:
            if calefactor.get_promocion():
                print(f'Marca: {calefactor.get_marca()}\nModelo: {calefactor.get_modelo()}\nPais de Fabricacion: {calefactor.get_paisfab()}\nImporte de venta: ${calefactor.get_impventa()}')