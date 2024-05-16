from models.empleado import Empleado


class GestorEmpleado:
    __empleados: list

    def __init__(self):
        self.__empleados = []
    
    def get_empleados(self):
        return self.__empleados
    
    def get_empleado(self, i):
        return self.__empleados[i]
    
    def agregar_empleado(self, empleado: Empleado):
        if isinstance(empleado, Empleado):
            self.__empleados.append(empleado)
    
    def mostrar_datos(self):
        for empleado in self.__empleados:
            print(empleado)
    
    def busqueda_id(self, id: int):
        valor_r = None
        i = 0
        while i < len(self.__empleados) and self.__empleados[i].get_id() != id:
            i += 1
        if i < len(self.__empleados):
            valor_r = i
        return valor_r
    
    def mostrar_datos_empleado(self, unempleado):
        if isinstance(unempleado, Empleado):
            print(unempleado)

    def get_matriculas(self, i: int):
        return self.__empleados[i].get_matricula()
    
    def mostrar_no_matriculados(self):
        for empleado in self.__empleados:
            if len(empleado.get_matricula()) == 0:
                print(f'El empleado {empleado.get_nombre()} no se registra ninguna matricula.')
    
    def validar_repeticion(self, xemp):
        valor_r = False
        if isinstance(xemp, Empleado):
            i = 0
            while i < len(self.__empleados) and self.__empleados[i] != xemp:
                i += 1
            if i < len(self.__empleados):
                valor_r = True
        else:
            raise TypeError('El elemento no es un Empleado.')
        return valor_r