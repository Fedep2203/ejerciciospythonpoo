from models.gestor_empleado import GestorEmpleado
from models.gestor_programa import GestorPrograma
from models.gestor_matricula import GestorMatricula

class Menu:
    __switcher: dict

    def __init__(self):
        self.__switcher = {
            '1': ('Buscar empleado por id e indicar duracion de capacitaciones.', self.opcion1),
            '2': ('Buscar participantes de un programa utilizando el nombre de este ultimo.', self.opcion2),
            '3': ('Indicar que empleados no realizaron capacitaciones.', self.opcion3),
            '4': ('Salir del programa', self.salir)
        }

    def mostrar_opc(self):
        for llave, valores in self.__switcher.items():
            print(f'{llave}) {valores[0]}')

    def selecc_opc(self, opc: str, gestorm: GestorMatricula, gestore: GestorEmpleado, gestorp: GestorPrograma):
        if opc == '1' or opc == '2':
            texto, funcion = self.__switcher[opc]
            print(texto)
            funcion(gestore, gestorp, gestorm)
        elif opc == '3':
            texto, funcion = self.__switcher[opc]
            print(texto)
            funcion(gestore)
        elif opc == '4':
            texto, funcion = self.__switcher[opc]
            print(texto)
            funcion()
        else:
            print('Opcion no valida. Intenta nuevamente.')
    
    def opcion1(self, gestore: GestorEmpleado, gestorp: GestorPrograma, gestorm: GestorMatricula):
        try:
            idbuscar = int(input('Ingrese el id del empleado a buscar.\n'))
            id = gestore.busqueda_id(idbuscar)
            print(id)
            if id != None:
                gestorm.mostrar_duracion(gestore.get_matriculas(id), gestorp)
            else:
                raise
        except ValueError:
            raise ValueError('Error: El ID debe ser un numero entero.')
    
    def opcion2(self, gestore: GestorEmpleado, gestorp: GestorPrograma, gestorm: GestorMatricula):
        nombrebuscar = str(input('Ingresa el nombre del programa a buscar.\n'))
        id = gestorp.busqueda_nombre(nombrebuscar)
        if id != None:
            gestorm.mostrar_empleados(gestorp.get_matriculas(id), gestore)
        else:
            print('Ningun programa tiene ese nombre.')
    
    def opcion3(self, gestore: GestorEmpleado):
        gestore.mostrar_no_matriculados()

    def salir(self):
        print('Adios...')
        del self