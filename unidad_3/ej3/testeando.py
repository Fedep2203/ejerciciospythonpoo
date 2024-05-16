from models.empleado import Empleado
from models.gestor_empleado import GestorEmpleado
import unittest

class testGestorEmpleado(unittest.TestCase):
    def setUp(self):
        self.__gestor = GestorEmpleado()
        unempleado = Empleado('Garcia Oriana', 123, 'Presidente Ejecutivo')
        otroempleado = Empleado('Ortiz Mariano', 456, 'Oficinista')
        self.__gestor.agregar_empleado(unempleado)
        self.__gestor.agregar_empleado(otroempleado)

    def testAgregarEmpleado(self):
        unempleado = Empleado('Garcia Oriana', 123, 'Presidente Ejecutivo')
        otroempleado = Empleado('Ortiz Mariano', 456, 'Oficinista')
        ultimoempleado = Empleado('Ortiz Marcos Aurelio', 654, 'Oficinista')
        lista = self.__gestor.get_empleados()
        self.assertEqual(len(lista), 2)
        self.assertIn(unempleado, lista)
        self.assertIn(otroempleado, lista)
        self.assertNotIn(ultimoempleado, lista)
    
    def testBusquedaId(self):
        idbuscar = 456
        id = self.__gestor.busqueda_id(456)
        self.assertNotEqual(id, None) #Busqueda exitosa
        idbuscar = 654
        id = self.__gestor.busqueda_id(654)
        self.assertEqual(id, None) #Busqueda Fallida
    
    def testValidarRepeticion(self):
        unempleado = Empleado('Garcia Oriana', 123, 'Presidente Ejecutivo')
        otroempleado = Empleado('Aurelio Marco', 100, 'Emperador')
        booleano = self.__gestor.validar_repeticion(unempleado)
        self.assertEqual(booleano, True)
        booleano = self.__gestor.validar_repeticion(otroempleado)
        self.assertNotEqual(booleano, True)

class testEmpleado(unittest.TestCase):
    def setUp(self):
        self.__empleado = Empleado('Garcia Oriana', 123, 'Presidente Ejecutivo')

    def testEqual(self):
        otro = Empleado('Ortiz Mariano', 456, 'Oficinista')
        self.assertNotEqual(otro, self.__empleado)



if __name__=='__main__':
    unittest.main()