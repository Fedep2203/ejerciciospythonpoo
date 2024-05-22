from models.publicacion import Publicacion


class AudioLibro(Publicacion):
    __narrador: str
    __tiemporep: float

    def __init__(self, titulo, categoria, preciobase, **datos):
        self.__narrador = datos['narrador']
        self.__tiemporep = datos['tiemporep']
        super().__init__(titulo, categoria, preciobase)
    
    def __str__(self):
        return f'Narrador: {self.__narrador} Duracion: {self.__tiemporep}\nTitulo: {super().get_titulo()} Categoria: {super().get_categoria() } Importe de Venta: {self.get_impventa()}'
    
    def get_impventa(self):
        return super().get_preciobase() + ((super().get_preciobase()*10)/100)