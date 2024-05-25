from models.lista import Lista
from models.calefactor_elec import CalefactorElec
from models.calefactor_gas import CalefactorGas
from models.objectencoder import ObjectEncoder

class Menu:
    __switcher: dict

    def __init__(self):
        self.__switcher = {

        }
    
    def mostrar_opc(self):
        for key, value in self.__switcher.items():
            print(f'{key}) {value[0]}')
    
    def opcion1(self, lista: Lista):
        #calefactorg = CalefactorGas('MarcaGX', 'ModeloXG', 'Luxemburgo', 250.0, 'cuotas', 6, 'no', 'ASD6547898', 2000)
        calefactore = CalefactorElec('MarcaRTX', 'ModeloXTZ', 'Argentina', 1000.0, 'contado', 1,'si', 1000)
        try:
            pos = int(input('Ingrese la posicion en la que desea agregar el calefactor.\n'))
            lista.insertar_enpos(pos, calefactore)
        except ValueError:
            print('Debes ingresar un valor entero.')
        except IndexError as error:
            print(error)
    
    def opcion2(self, lista: Lista):
        metodos = ['cuotas', 'contado']
        tipo = str(input('Ingresa el tipo de calefactor que deseas registrar ("gas" o "electrico").\n'))
        if tipo == "gas" or tipo == "electrico":
            try:
                calef = None
                marca = str(input('Ingrese.\n'))
                modelo = str(input('Ingrese.\n'))
                paisfab = str(input('Ingrese.\n'))
                preciolista = float(input('Ingrese.\n'))
                metodopago = str(input('Ingrese.\n'))
                if metodopago in metodos:
                    if metodopago == 'contado':
                        cuotas = 1
                        promo = str(input('Ingrese.\n'))
                    else:
                        cuotas = int(input('Ingrese.\n'))
                        promo = "no"
                    if tipo == "gas":
                        matricula = str(input('Ingrese.\n'))
                        calorias = float(input('Ingrese.\n'))
                        calef = CalefactorGas(marca, modelo, paisfab, preciolista, metodopago, cuotas, promo, matricula, calorias)
                    else:
                        potencia = float(input('Ingrese.\n'))
                        calef = CalefactorElec(marca, modelo, paisfab, preciolista, metodopago, cuotas, promo, potencia)
                    lista.insertar_final()
                else:
                    raise ValueError('Metodo de pago invalido')

            except ValueError as e:
                print(e)

    def opcion3(self, lista: Lista):
        try:
            pos = int(input('Ingrese la posicion en la que desea agregar el calefactor.\n'))
            lista.mostrar_datoesp(pos)
        except ValueError:
            print('Debes ingresar un valor entero.')
        except IndexError as error:
            print(error)
    
    def opcion4(self, lista: Lista):
        lista.menor_precio_gas()

    def opcion5(self, lista: Lista):
        marca = str(input('Ingrese marca a buscar.\n'))
        lista.mostrar_modelos_elec(marca)

    def opcion6(self, lista: Lista):
        lista.mostrar_datospromo()
    
    def opcion7(self, lista: Lista,lector: ObjectEncoder):
        diccionario = lista.tojson()
        lector.guardar_json('calefactores.json', diccionario)
        

    def salir(self):
        print('Saliendo del progama...')
        del self