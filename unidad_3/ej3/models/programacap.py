class ProgramaCapacitacion:
    __nombre: str
    __codigo: str
    __duracion: int
    __matriculas: list

    def __init__(self, nombre: str, codigo: str, duracion: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
        self.__matriculas = []
    
    def __str__(self):
        return f'Nombre: {self.__nombre} Codigo: {self.__codigo}'
    
    def agregar_matricula(self, matricula):
        self.__matriculas.append(matricula)
    
    def get_matricula(self):
        return self.__matriculas
    
    def get_nombre(self):
        return self.__nombre
    
    def get_duracion(self):
        return self.__duracion

    def get_codigo(self):
        return self.__codigo
    
    def __eq__(self, otro):
        valor_r = False
        if isinstance(otro, ProgramaCapacitacion):
            if self.get_nombre() == otro.get_nombre():
                if self.get_codigo() == otro.get_codigo():
                    if self.get_duracion() == otro.get_duracion():
                        valor_r = True
        return valor_r
