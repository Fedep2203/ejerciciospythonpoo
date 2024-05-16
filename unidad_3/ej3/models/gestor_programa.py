from models.programacap import ProgramaCapacitacion

class GestorPrograma:
    __programas: list

    def __init__(self):
        self.__programas = []

    def agregar_programa(self, programa):
        if isinstance(programa, ProgramaCapacitacion):
            self.__programas.append(programa)
        else:
            raise TypeError('El elemento no es una instancia de la clase ProgramaCapacitacion.')
    
    def busqueda_nombre(self, nombre):
        valor_r = None
        i = 0
        while i < len(self.__programas) and self.__programas[i].get_nombre() != nombre:
            i += 1
        if i < len(self.__programas):
            valor_r = i
        return valor_r
    
    def mostrar_datos_programa(self, unprograma):
        if isinstance(unprograma, ProgramaCapacitacion):
            print(f'La duracion del programa {unprograma.get_nombre()} es de {unprograma.get_duracion()}')
        else:
            raise TypeError('El elemento no es una instancia de la clase ProgramaCapacitacion.')
    
    def get_matriculas(self, i):
        return self.__programas[i].get_matricula()

    def mostrar_datos(self):
        for programa in self.__programas:
            print(programa)
    
    def validar_repeticion(self, xprograma):
        valor_r = False
        if isinstance(xprograma, ProgramaCapacitacion):
            i = 0
            while i < len(self.__programas) and self.__programas[i] != xprograma:
                i += 1
            if i < len(self.__programas):
                valor_r = True
        else:
            raise TypeError('El elemento no es un programa.')
        return valor_r
    
    def get_programa(self, i):
        return self.__programas[i]