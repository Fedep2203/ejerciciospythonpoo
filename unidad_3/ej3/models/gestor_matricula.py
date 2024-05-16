from models.matricula import Matricula

class GestorMatricula:
    def mostrar_duracion(self, matriculas, gestorp):
        from models.gestor_programa import GestorPrograma
        for matricula in matriculas:
            gestorp.mostrar_datos_programa(matricula.get_programa())
    
    def mostrar_empleados(self, matriculas, gestore):
        from models.gestor_empleado import GestorEmpleado
        for matricula in matriculas:
            gestore.mostrar_datos_empleado(matricula.get_empleado())