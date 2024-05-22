from models.audiolibro import AudioLibro
from models.libro import Libro
from models.publicacion import Publicacion

class Nodo:
    __publicacion: Publicacion
    __siguiente: object

    def __init__(self, publicacion):
        self.__publicacion = publicacion
        self.__siguiente = None

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def get_dato(self):
        return self.__publicacion
    
    def get_siguiente(self):
        return self.__siguiente

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__indice = 0
        self.__tope = 0
        self.__comienzo = None
    
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            datos = self.__actual.get_dato()
            self.__indice += 1
            self.__actual = self.__actual.get_siguiente()
            return datos
    
    def agregar_publicacion(self, publicacion):
        nodo = Nodo(publicacion)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def buscar_posicion(self, pos: int):
        if pos <= self.__tope:
            pos -= 1
            aux = self.__comienzo
            encontrado = False
            i = 0
            dato = None
            while aux != None and not encontrado:
                if i == pos:
                    encontrado = True
                    dato = aux.get_dato()
                else:
                    aux = aux.get_siguiente()
                    i += 1
            print(dato)
            if isinstance(dato, Libro):
                print('La publicacion corresponde a un Libro')
            if isinstance(dato, AudioLibro):
                print('La publicacion corresponde a un AudioLibro')
        else:
            raise IndexError('La posicion se encuentra fuera de los limites de la coleccion.')
    
    def mostrar_cantidad(self):
        contl = 0
        contal = 0
        for publicacion in self:
            if isinstance(publicacion, Libro):
                contl += 1
            if isinstance(publicacion, AudioLibro):
                contal += 1
        print(f'La cantidad de publicaciones que corresponden a libros es de {contl}')
        print(f'La cantidad de publicaciones que corresponden a AudioLibros es de {contal}')
    
    def mostrar_datos(self):
        for publicacion in self:
            print(publicacion)
            
    
        
