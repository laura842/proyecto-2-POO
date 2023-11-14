from model.aerolineaModel import AerolineaModel
from model.aeropuertoModel import AeropuertoModel
from model.puertaDeEmbarqueModel import PuertaDeEmbarqueModel
from view.aeropuertoView import AeropuertoView


class AeropuertoCont:
    def __init__(self):
        self.model = AeropuertoModel()
        self.view = AeropuertoView()

        self.aeronavesCount = 0
        self.aerolineasCount = 0
        self.puertasCount = 0

    def increaseAeronavesCount(self):
        self.aeronavesCount = self.aeronavesCount + 1
        return self.aeronavesCount

    def increaseAerolineasCount(self):
        self.aerolineasCount = self.aerolineasCount + 1
        return self.aerolineasCount

    def increasePuertasCount(self):
        self.puertasCount = self.puertasCount + 1
        return self.puertasCount

    def createNewAerolinea(self):
        self.view.addNewAerolinea()
        listaDestinos = []
        nombre = self.view.askValue("Ingrese el nombre de la aerolinea: ")
        destino = self.view.askValue("Ingrese un destino de la aerolinea (si no desea ingresar más destinos, "
                                     "presione enter): ")

        while destino != "":
            listaDestinos.append(destino)
            destino = self.view.askValue("Ingrese un destino de la aerolinea (si no desea ingresar más destinos, "
                                         "presione enter): ")

        print("Los vuelos se podran anadir posteriormente.")

        newAerolinea = AerolineaModel(nombre, listaDestinos)
        self.model.addAerolinea(self.increaseAerolineasCount(), newAerolinea)

    def createNewPuerta(self):
        self.view.addNewPuerta()
        idP = self.view.askValue("Ingrese el ID de la puerta: ")
        ubicacion = self.view.askValue("Ingrese la ubicacion de la puerta: ")
        """
        flag = input("Ingrese 1 si desea agregar un vuelo. En caso de que no, ingrese 0")
        while flag != 1 or flag != 0:
            print("Valor no válido, intente de nuevo")
            flag = input("Ingrese 1 si desea agregar un vuelo. En caso de que no, ingrese 0")
        if flag == 1:
            idV = self.view.askValue("Ingrese el ID del vuelo: ")

            fecha = self.view.askValue("Ingrese la fecha del vuelo: ")
            origen = self.view.askValue("Ingrese el origen del vuelo: ")
            destino = self.view.askValue("Ingrese el destino del vuelo: ")

            flag2 = input("Ingrese 1 si desea crear una aeronave. Si desea usar una aeronave ya existente, ingrese 2")
            while flag2 != 1 or flag2 != 2:
                print("Valor no válido, intente de nuevo")
                flag2 = input("Ingrese 1 si desea agregar un vuelo. Si desea usar una aeronave ya existente, ingrese 2")
            if flag2 == 1:
                print("- Nuevo vuelo -")
            elif flag2 == 2:
                print("Seleccione de la lista de vuelos a continuación")
        """
        newPuerta = PuertaDeEmbarqueModel(idP, ubicacion)
        self.model.addPuerta(self.increasePuertasCount(), newPuerta)

    def createNewAeronave(self):
        self.view.addNewAeronave()
        idA = self.view.askValue("Ingrese el ID de la aeronave: ")
        marca = self.view.askValue("Ingrese la marca de la aeronave: ")
        modelo = self.view.askValue("Ingrese el modelo de la aeronave: ")
        capacidad = self.view.askValue("Ingrese la capacidad de la aeronave: ")
        velMax = self.view.askValue("Ingrese la velociad maxima de la aeronave: ")
        autonomia = self.view.askValue("Ingrese la autonomia de la aeronave: ")
        anioFab = self.view.askValue("Ingrese el anio de fabricacion de la aeronave: ")


