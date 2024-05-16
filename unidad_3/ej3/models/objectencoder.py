import json
from pathlib import Path
from models.gestor_empleado import GestorEmpleado
from models.empleado import Empleado
from models.gestor_matricula import GestorMatricula, Matricula
from models.gestor_programa import GestorPrograma, ProgramaCapacitacion

class ObjectEncoder:
    def decodificar_dict(self, d, gestore: GestorEmpleado, gestorp: GestorPrograma):
        valor_r = False
        if '__class__' not in d:
            valor_r = d
        else:
            class_name = d['__class__']
            if class_name == 'GestorMatricula':
                matriculas = d['matriculas']
                matricula = matriculas[0]
                for i in range(len(matriculas)):
                    matricula = matriculas[i]
                    atributos = matricula['__atributos__']
                    programa = self.decodificar_dictpro(atributos['programa'])
                    empleado = self.decodificar_dictemp(atributos['empleado'])
                    class_name = matricula.pop('__class__')
                    class_ = eval(class_name)
                    if gestore.validar_repeticion(empleado) == False:
                        gestore.agregar_empleado(empleado)
                    if gestorp.validar_repeticion(programa) == False:
                        gestorp.agregar_programa(programa)                    
                    matri = class_(atributos['fecha'], gestore.get_empleado(gestore.busqueda_id(empleado.get_id())), gestorp.get_programa(gestorp.busqueda_nombre(programa.get_nombre())))
                    valor_r = True
        return valor_r
    
    def decodificar_dictemp(self, d):
        valor_r = None
        if '__class__' not in d:
            valor_r = d
        else:
            class_name = d['__class__']
            if class_name == 'Empleado':
                class_ = eval(class_name)
                atributos = d['__atributos__']
                empleado = class_(**atributos)
                valor_r = empleado
        return valor_r
    
    def decodificar_dictpro(self, d):
        valor_r = None
        if '__class__' not in d:
            valor_r = d
        else:
            class_name = d['__class__']
            if class_name == 'ProgramaCapacitacion':
                class_ = eval(class_name)
                atributos = d['__atributos__']
                programa = class_(**atributos)
                valor_r = programa
        return valor_r
    
    def leerJSON(self, archivo):
        valor_r = None
        with Path(archivo).open(encoding='utf-8') as fuente:
            valor_r = json.load(fuente)
        return valor_r
    
    def guardarJSON(self, archivo, diccionario):
        with Path(archivo).open('w', encoding='utf-8') as destino:
            json.dump(diccionario, destino, indent=4)

            
