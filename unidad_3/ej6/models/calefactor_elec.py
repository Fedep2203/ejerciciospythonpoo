from models.calefactor import Calefactor

class CalefactorElec(Calefactor):
    __potencia: float

    def __init__(self, marca: str, modelo: str, paisfab: str,
                  preciolista: float, metodo: str, cuotas: int, promo: str, potencia: float):
       super().__init__(marca, modelo, paisfab, preciolista, metodo, cuotas, promo)
       self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def get_impventa(self):
        valor_r = 0
        if self.__metodopago.lower() == 'contado':
            if self.__promocion:
                valor_r = super().get_preciolista() - ((super().get_preciolista()*15)/100)
            else:
                valor_r = super().get_preciolista()
        elif self.__metodopago.lower() == 'cuotas':
            valor_r = super().get_preciolista() + ((super().get_preciolista()*40)/100)
        if self.__potencia >= 1000:
            valor_r += super().get_preciolista()/100
        return valor_r
    
    def tojson(self):
        diccionario = {
            '__class__': self.__class__.__name__,
            '__atributos__': {
                'marca': super().get_marca(),
                'modelo': super().get_modelo(),
                'paisfab': super().get_paisfab(),
                'preciolista': super().get_preciolista(),
                'metodopago': super().get_metodopago(),
                'cuotas': super().get_cuotas(),
                'promo': super().get_promocion(),
                'potencia': self.__potencia
            }
        }
        return diccionario

    def __str__(self):
        return f'Marca: {super().get_marca()} Modelo: {super().get_modelo()}\nPotencia: {self.__potencia:2f}watts Tipo: Electrico'


