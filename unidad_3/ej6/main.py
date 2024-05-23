from models.calefactor_gas import CalefactorGas
from models.calefactor_elec import CalefactorElec
from models.lista import Lista

calefactor1 = CalefactorElec("MarcaA", "ModeloX", "Argentina", 15000.0, "cuotas", 12, "no", 900.0)
calefactor2 = CalefactorGas("MarcaB", "ModeloY", "Brasil", 20000.0, "contado", 1, "si", "ABC125437", 2000.0)
calefactor3 = CalefactorGas("MarcaC", "ModeloZ", "Chile", 18000.0, "contado", 1, "si", "ABC1234567", 3500.0)
calefactor4 = CalefactorGas("MarcaD", "ModeloW", "Perú", 16000.0, "cuotas", 6, "no", "XYZ9876543", 3000.0)
calefactor5 = CalefactorElec("MarcaE", "ModeloV", "Uruguay", 22000.0, "contado", 1, "si", 2000.0)
calefactor6 = CalefactorElec("MarcaF", "ModeloU", "Colombia", 19000.0, "cuotas", 10, "no", 1500.0)
lista = Lista()
lista.insertar_inic(calefactor1)
lista.insertar_inic(calefactor2)
lista.insertar_inic(calefactor3)
lista.insertar_inic(calefactor4)
lista.insertar_enpos(3, calefactor5)
lista.insertar_final(calefactor6)
for calef in lista:
    print(calef)