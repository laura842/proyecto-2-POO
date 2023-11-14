from aeronaveModel import AeronaveModel


# Definir una clase 'Avion' con atributos y metodos
class AvionModel(AeronaveModel):
    # Metodo constructor
    def __init__(self, idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign, ubicacion, altitudMax,
                 motores, categoria):
        super().__init__(idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign, ubicacion)
        self.__altitudMax = altitudMax
        self.__motores = motores
        self.__categoria = categoria

    def imprimirDatosAv(self):
        super().imprimirDatosAero()
        print("Altitud maxima: {}".format(self.__altitudMax))
        print("Cantidad de motores: {}".format(self.__motores))
        print("Categoria: {}".format(self.__categoria))

    # Setters

    def setAltitud(self, nAlt):
        self.__altitudMax = nAlt

    def setMotores(self, nMot):
        self.__motores = nMot

    def setCategoria(self, nCat):
        self.__categoria = nCat

    def getAltitudMaxima(self):
        return self.__altitudMax
