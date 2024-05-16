class Empleado:
    __ayn: str
    __id: int
    __puesto: str
    __matriculas: list

    def __init__(self, ayn: str, id: int, puesto: str):
        self.__ayn = ayn
        self.__id = id
        self.__puesto = puesto
        self.__matriculas = []
    
    def agregar_matricula(self, matricula):
        self.__matriculas.append(matricula)

    def __str__(self):
        return f'Nombre: {self.get_nombre()} Puesto: {self.get_puesto()}'
    
    def get_nombre(self):
        return self.__ayn
    
    def get_id(self):
        return self.__id
    
    def get_matricula(self):
        return self.__matriculas
    
    def get_puesto(self):
        return self.__puesto
    
    def __eq__(self, otro):
        valor_r = False
        if isinstance(otro, Empleado):
            if self.get_id() == otro.get_id():
                if self.get_nombre() == otro.get_nombre():
                    if self.get_puesto() == otro.get_puesto():
                        valor_r = True
        return valor_r
