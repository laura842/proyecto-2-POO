
# Definir una clase 'PuertaDeEmbarque' con atributos y metodos
class PuertaDeEmbarqueModel:
    # Metodo constructor
    def __init__(self, numPuerta, ubicacion, vueloActual="", horaEmbarque="", historial=None):
        if historial is None:
            historial = []
        self.__numPuerta = numPuerta
        self.__ubicacion = ubicacion
        self.__disponible = True
        self.__horaEmbarque = horaEmbarque
        self.___vueloActual = vueloActual
        self.__historial = historial

    def anadirAlHistorial(self, newVuelo):
        self.__historial.append(newVuelo)

    # Setters

    def setNumPuerta(self, newNum):
        self.__numPuerta = newNum

    def setUbicacion(self, newUb):
        self.__ubicacion = newUb

    def setDisponible(self, newDisp):
        self.__disponible = newDisp

    def setHoraEmbarque(self, newHora):
        self.__horaEmbarque = newHora

    def setVueloActual(self, newVuelo):
        self.___vueloActual = newVuelo

    # Getters

    def getNumPuerta(self):
        return self.__numPuerta

    def getUbicacion(self):
        return self.__ubicacion

    def getDisponible(self):
        return self.__disponible

    def getHoraEmbarque(self):
        return self.__horaEmbarque

    def getVueloActual(self):
        return self.___vueloActual

    def getHistorial(self):
        return self.__historial
