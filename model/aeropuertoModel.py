# Definir una clase 'Aeropuerto' con atributos y metodos


"""
class Aeropuerto:
    __instance = None

    @staticmethod
    def getInstance(aeronaves, aerolineas, puertas):
        if Aeropuerto.__instance is None:
            Aeropuerto(aeronaves, aerolineas, puertas)
        return Aeropuerto.__instance

    def __init__(self, aeronaves, aerolineas, puertas):
        if Aeropuerto.__instance is not None:
            raise Exception("Ya existe el aeropuerto")
        Aeropuerto.__instance = self
        self.__aeronaves = aeronaves
        self.__aerolineas = aerolineas
        self.__puertas = puertas
"""


class AeropuertoModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AeropuertoModel, cls).__new__(cls)
        return cls._instance

    # Metodo constructor
    def __init__(self):
        self.__aeronaves = {}
        self.__aerolineas = {}
        self.__puertas = {}

    # Getters

    def getAeronaves(self):
        return self.__aeronaves

    def getAerolineas(self):
        return self.__aerolineas

    def getPuertas(self):
        return self.__puertas

    # Setters
    # Otros

    def addAeronave(self, idAn, newAeronave):
        self.__aeronaves[idAn] = newAeronave
        print("Se ha anadido la aeronave:")
        print(newAeronave)

    def addAerolinea(self, idAl, newAerolinea):
        self.__aerolineas[idAl] = newAerolinea
        print("Se ha anadido la aerolinea:")
        print(newAerolinea)

    def addPuerta(self, idP, newPuerta):
        self.__puertas[idP] = newPuerta
        print("Se ha anadido la puerta:")
        print(newPuerta)

    """
    def printAeronaves(self):
        print("Estas son todas las aeronaves del aeropuerto:")
        print(self.__aeronaves)

    def printAerolineas(self):
        print("Estas son todas las aerolineas que trabajan con nosotros:")
        print(self.__aerolineas)

    def printPuertas(self):
        print("estas son todas las puertas de embarque del aeropuerto:")
        print(self.__puertas)

    """

    # Buscar y reservar vuelos se hace con la aerolinea
