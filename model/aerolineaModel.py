# Definir una clase 'Aerolinea' con atributos y metodos
class AerolineaModel:
    # Metodo constructor
    def __init__(self, nombre, destinos=None):
        if destinos is None:
            destinos = []
        self.nombre = nombre
        self.destinos = destinos
        self.vuelos = []

    def verVuelos(self, fecha1, origen, destino):
        contador = 0
        for i in self.vuelos:
            if (self.vuelos[i].getOrigen == origen and self.vuelos[i].getDestino() == destino and
                    self.vuelos[i].getFecha() == fecha1):
                print("El vuelo " + self.vuelos[i].getId() + " se encuentra disponible en la fecha " + fecha1
                      + " con destino a " + destino)
                contador += 1

        if contador == 0:
            print("No hay vuelos con esas especificaciones disponibles por el momento")

    def reservarVuelo(self, idV):
        flag = False
        for i in self.vuelos:
            if self.vuelos[i].getId() == idV:
                if self.vuelos[i].getSillasDisp() > 0:
                    "self.vuelos[i].anadirPasajero(pasajero)"
                    print("Vuelo reservado correctamente")
                else:
                    print("No hay sillas disponibles para el vuelo " + idV)

                flag = True

        if not flag:
            print("No existe un vuelo con el id " + idV)
