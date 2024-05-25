import json
from pathlib import Path
from models.lista import Lista
from models.calefactor_elec import CalefactorElec
from models.calefactor_gas import CalefactorGas

class ObjectEncoder:
    def guardar_json(self, archivo: str, diccionario: dict):
        with Path(archivo).open('w', encoding='utf-8') as destino:
            json.dump(diccionario, destino, indent = 4)
            destino.close()

    def leer_json(self, archivo):
        diccionario = None
        with Path(archivo).open('r', encoding='utf-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def decodificar(self, diccionario: dict):
        valor_r = diccionario
        if '__class__' in diccionario:
            class_name = diccionario['__class__']
            if class_name == 'Lista':
                class_ = eval(class_name)
                lista = class_()
                calefactores = diccionario['calefactores']
                for calefactor in calefactores:
                    class_name = calefactor['__class__']
                    atributos = calefactor['__atributos__']
                    class_ = eval(class_name)
                    calef = class_(**atributos)
                    lista.insertar_inic(calef)
                valor_r = lista
        return valor_r
        