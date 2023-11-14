from aeronaveModel import AeronaveModel


# Definir una clase 'Helicoptero' con atributos y metodos
class HelicopteroModel(AeronaveModel):
    # Metodo constructor
    def __init__(self, idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign, ubicacion, rotores,
                 capElevacion, usoEsp):
        super().__init__(idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign, ubicacion)
        self.__rotores = rotores
        self.__capElevacion = capElevacion
        self.__usoEsp = usoEsp

    def imprimirDatosH(self):
        super().imprimirDatosAero()
        print("Cantidad de rotores: {}".format(self.__rotores))
        print("Capacidad de elevación: {}".format(self.__capElevacion))
        print("Uso especifico: {}".format(self.__usoEsp))

    # Setters

    def setRotores(self, nRot):
        self.__rotores = nRot

    def setCapElevacion(self, nCapE):
        self.__capElevacion = nCapE

    def setUsoEsp(self, nUso):
        self.__usoEsp = nUso

    def getRotores(self):
        return self.__rotores
