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
    
    def insertar_enpos(self, pos: int, dato: object):
        aux = self.__cabeza
        if aux == None or pos == 1:
            nodo = Nodo(dato)
            nodo.set_siguiente(self.__cabeza)
            self.__cabeza = nodo
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
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
        
    def insertar_final(self, dato: object):
        aux = self.__cabeza
        anterior = None
        while aux != None:
            anterior = aux
            aux = aux.get_siguiente()
        nodo = Nodo(dato)
        nodo.set_siguiente(aux)
        anterior.set_siguiente(nodo)
    
    def mostrar_datoesp(self, pos: int):
        if 0 < pos <= self.__tope:
            aux = self.__cabeza
            if aux == None:
                print('La lista se encuentra vacia'):
            else:
                i = 0
                while aux != None and i < self.__tope:
                    anterior = aux
                    aux = aux.get_siguiente()
                    i += 1
                if anterior == None:
                    print('El elemento no existe.')
                else:
                    print(anterior.get_dato())
        else:
            raise IndexError('La posicion ingresada excede el rango de la lista.')
