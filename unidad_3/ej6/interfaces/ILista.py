from zope.interface import Interface

class ILista(Interface):
    def insertar_enpos(pos: int, dato: object):
        pass

    def insertar_final(dato: object):
        pass

    def mostrar_datoesp(pos: int):
        pass