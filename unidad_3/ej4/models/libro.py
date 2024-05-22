from datetime import datetime
from models.publicacion import Publicacion



class Libro(Publicacion):
    __nombreautor: str
    __fechaedicion: int
    __cantpaginas: int

    def __init__(self, titulo, categoria, preciobase, **datos):
        self.__nombreautor = datos['autor']
        self.__fechaedicion = datos['fecha']
        self.__cantpaginas = datos['cantpaginas']
        super().__init__(titulo, categoria, preciobase)

    def get_fecha(self):
        return self.__fechaedicion

    def __str__(self):
        return f'Autor: {self.__nombreautor} Cantidad de Paginas: {self.__cantpaginas}\nTitulo: {super().get_titulo()} Categoria: {super().get_categoria()} Importe de venta = {self.get_impventa()}'
    
    def get_impventa(self):
        porcentaje = (super().get_preciobase()*1)/100
        diferencia = datetime.now().year - self.get_fecha()
        return super().get_preciobase() - (porcentaje * diferencia)