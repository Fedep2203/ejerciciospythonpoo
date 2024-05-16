from models.objectencoder import ObjectEncoder
from models.gestor_matricula import GestorMatricula
from models.gestor_empleado import GestorEmpleado, Empleado
from models.gestor_programa import GestorPrograma
from models.menu import Menu



def main():
    jsonF = ObjectEncoder()
    gestorm = GestorMatricula()
    gestore = GestorEmpleado()
    empleado = Empleado('Morales Agustin', 963, 'Ingeniero de Software')
    gestore.agregar_empleado(empleado) #Empleado sin matricula
    gestorp = GestorPrograma( )
    dicc = jsonF.leerJSON('matriculas.json')
    jsonF.decodificar_dict(dicc, gestore, gestorp)
    menu = Menu()
    opc = '-1'
    while opc != '4':
        menu.mostrar_opc()
        opc = str(input('Ingresar opcion:\n'))
        menu.selecc_opc(opc, gestorm, gestore, gestorp)


if __name__ == '__main__':
    main()