
class AeropuertoView:

    def askValue(self, message):
        return input(message)

    def addNewAerolinea(self):
        print("- Creación de nueva aerolinea -")

    def removeAerolinea(self):
        print("- Eliminación de una aerolinea -")

    def addNewAeronave(self):
        print("- Creación de nueva aeronave -")

    def removeAeronave(self):
        print("- Eliminación de una aeronave -")

    def addNewPuerta(self):
        print("- Creación de nueva puerta -")

    def removePuerta(self):
        print("- Eliminación de una puerta -")

    def listAllAerolineas(self, aerolineas):
        print("- Visualizacion de aerolineas -")
        for aerolinea in aerolineas:
            singleAerolinea = aerolineas[aerolinea]
            print(f"Nombre de la aerolinea: {singleAerolinea.nombre}")
            for destino in singleAerolinea.destinos:
                print(f"Destino: {destino}")
            """
            for vuelo in singleAerolinea.vuelos:
                print(f"")
            """

    def listAllAeronaves(self, aeronaves):
        print("- Visualizacion de aeronaves -")
        print("~ Aviones ~")
        for avion in aeronaves:
            if aeronaves[avion].getAltitudMaxima(aeronaves[avion]) > 0:
                aeronaves[avion].imprimirDatosAv(aeronaves[avion])

        print("~ Helicopteros ~")
        for helicoptero in aeronaves:
            if aeronaves[helicoptero].getRotores(aeronaves[helicoptero]) > 0:
                aeronaves[helicoptero].imprimirDatosH(aeronaves[helicoptero])

        print("~ Jets privados ~")
        for jet in aeronaves:
            if len(aeronaves[jet].getServicios(aeronaves[jet])) > 0:
                aeronaves[jet].imprimirDatosJet(aeronaves[jet])

    def listAllPuertas(self, puertas):
        print("- Visualizacion de Puertas de Embarque -")
        for puerta in puertas:
            singlePuerta = puertas[puerta]
            print(f"Numero de la puerta: {singlePuerta.getNumPuerta()}")
