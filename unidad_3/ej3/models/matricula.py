from models.empleado import Empleado
from models.programacap import ProgramaCapacitacion

class Matricula:
    __fecha: str
    __empleado: object
    __programa: object

    def __init__(self, fecha: str, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa
        self.__empleado.agregar_matricula(self)
        self.__programa.agregar_matricula(self)

    def __str__(self):
        return f'Fecha: {self.__fecha} Empleado: {self.__empleado.get_nombre()} Programa: {self.__programa.get_nombre()}'
    
    def get_programa(self):
        return self.__programa
    
    def get_empleado(self):
        return self.__empleado
    