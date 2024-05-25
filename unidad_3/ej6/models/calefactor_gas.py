from models.calefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula: str
    __calorias: str

    def __init__(self, marca: str, modelo: str, paisfab: str, preciolista: float, metodopago: str,
                 cuotas: int, promo: str, matricula: str, calorias: float):
        super().__init__(marca, modelo, paisfab, preciolista, metodopago, cuotas, promo)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def tojson(self):
        promo = None
        if super().get_promocion():
            promo = 'si'
        else:
            promo = 'no'
        diccionario = {
            '__class__': self.__class__.__name__,
            '__atributos__': {
                'marca': super().get_marca(),
                'modelo': super().get_modelo(),
                'paisfab': super().get_paisfab(),
                'preciolista': super().get_preciolista(),
                'metodopago': super().get_metodopago(),
                'cuotas': super().get_cuotas(),
                'promo': promo,
                'matricula': self.__matricula,
                'calorias': self.__calorias
            }
        }
        return diccionario

    def get_preciolista(self):
        return super().get_preciolista()
    
    def get_matricula(self):
        return self.__matricula
    
    def get_calorias(self):
        return self.__calorias
    
    def get_impventa(self):
        valor_r = 0
        if self.get_metodopago().lower() == 'contado':
            if self.get_promocion():
                valor_r = super().get_preciolista() - ((super().get_preciolista()*15)/100)
            else:
                valor_r = super().get_preciolista()
        elif self.get_metodopago().lower() == 'cuotas':
            valor_r = super().get_preciolista() + ((super().get_preciolista()*40)/100)
        if self.__calorias >= 3000:
            valor_r += super().get_preciolista()/100
        return valor_r
    
    def __str__(self):
        return f'Marca: {super().get_marca()} Modelo: {super().get_modelo()}\nMatricula: {self.__matricula} Calorias: {self.__calorias:.2f}/m3 Tipo: Gas'