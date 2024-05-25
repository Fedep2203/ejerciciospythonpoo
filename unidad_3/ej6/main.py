from models.objectencoder import ObjectEncoder
from models.calefactor_elec import CalefactorElec
from models.lista import Lista

def main():
    lector = ObjectEncoder()
    diccionario = lector.leer_json('calefactores.json')
    lista = lector.decodificar(diccionario)
    calefactore = CalefactorElec('MarcaRTX', 'ModeloXTZ', 'Argentina', 1000.0, 'contado', 1,'si', 1000)
    lista.insertar_inic(calefactore)
    lista.mostrar_modelos_elec('MarcaE')
    lista.mostrar_datospromo()
    lista.menor_precio_gas()
    lector.guardar_json('calefactores.json', lista.tojson())


if __name__ == '__main__':
    main()

