from models.lista import Lista
from models.menu import Menu


def main():
    lista = Lista()
    menu = Menu()
    opc = '-1'
    while opc != '5':
        menu.mostrar_opc()
        opc = str(input('Ingresa una opcion.\n'))
        menu.selecc_opc(lista, opc)
    print('El programa finalizo.')

if __name__ == '__main__':
    main()