from models.lista import Lista
from models.libro import Libro
from models.audiolibro import AudioLibro

class Menu:
    __switchter: dict

    def __init__(self):
        self.__switchter = {
            '1': ('Agregar publicaciones a la coleccion.', self.opcion1),
            '2': ('Buscar una posicion y mostrar el tipo de Publicacion.', self.opcion2),
            '3': ('Mostrar cantidad de libros y audiolibros en la coleccion.', self.opcion3),
            '4': ('Mostrar datos de las publicaciones y su importe de venta.', self.opcion4),
            '5': ('Salir del programa', self.salir)
        }
    
    def mostrar_opc(self):
        for llave, datos in self.__switchter.items():
            print(f'{llave}) {datos[0]}')
    
    def selecc_opc(self, lista: Lista, opc: str):
        if opc in ['1', '2', '3', '4']:
            texto, funcion = self.__switchter[opc]
            print(texto)
            funcion(lista)
        elif opc == '5':
            texto, funcion = self.__switchter[opc]
            print(texto)
            funcion()
        else:
            print('Intenta nuevamente.')

    def opcion1(self, lista: Lista):
        libro = Libro('Limpiador de codigo', 'Tecnologia', 24.50, autor='Sergio Pacheco Coria', fecha=2004, cantpaginas=450)
        libro1 = Libro('Intrascendentes Tardias', 'Ciencia', 20.0, autor='Santiago Vilchez Reinoso', fecha=1990, cantpaginas=700)
        alibro = AudioLibro('Jujutsu Kaisen', 'Manga', 50.0, narrador='el primo de pacheco', tiemporep=45.0)
        alibro1 = AudioLibro('Design Patterns Elements of Reusable Object-Oriented Software',
                              'Tecnologia', 100.25, narrador='Antonio Ortiz', tiemporep=70.0)
        lista.agregar_publicacion(libro)
        lista.agregar_publicacion(libro1)
        lista.agregar_publicacion(alibro)
        lista.agregar_publicacion(alibro1)
    
    def opcion2(self, lista: Lista):
        try:
            pos = int(input('Ingresa la posicion de la que se desea extraer el dato.\n'))
            lista.buscar_posicion(pos)
        except IndexError as e:
            print(e)
        except ValueError:
            print('Debes ingresar un numero entero.')

    def opcion3(self, lista: Lista):
        lista.mostrar_cantidad()
    
    def opcion4(self, lista: Lista):
        lista.mostrar_datos()

    def salir(self):
        print('Saliendo del programa.')
        del self