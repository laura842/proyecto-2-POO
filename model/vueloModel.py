
# Definir una clase 'Vuelo' con atributos y metodos
class VueloModel:
    # Metodo constructor
    def __init__(self, idV, fecha, origen, destino, aeronaveAsign, puertaAsign, sillasDisp, tripAsign, pasajerosV):
        self.__idV = idV
        self.__fecha = fecha
        self.__origen = origen
        self.__destino = destino
        self.aeronaveAsign = aeronaveAsign
        self.puertaAsign = puertaAsign
        self.__sillasDisp = sillasDisp
        self.tripAsign = tripAsign
        self.pasajerosV = pasajerosV

    def getIdV(self):
        return self.__idV

    def getOrigen(self):
        return self.__origen

    def getDestino(self):
        return self.__destino

    def getFecha(self):
        return self.__fecha

    def getSillasDisp(self):
        return self.__sillasDisp
