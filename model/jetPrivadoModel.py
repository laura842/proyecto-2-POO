from aeronaveModel import AeronaveModel


# Definir una clase 'JetPrivado' con atributos y metodos
class JetPrivadoModel(AeronaveModel):
    # Metodo constructor
    def __init__(self, idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign, ubicacion, propietario,
                 serviciosABordo, destinosFrecuentes):
        super().__init__(idA, marca, modelo, capacidad, velMax, autonomia, anioFab, totalAsign,
                         ubicacion)
        self.__propietario = propietario
        self.__serviciosABordo = serviciosABordo
        self.__destinosFrecuentes = destinosFrecuentes

    def imprimirDatosJet(self):
        super().imprimirDatosAero()
        print("Propietario: {}".format(self.__propietario))
        print("Servicios a bordo: {}".format(self.__serviciosABordo))
        print("Destinos frecuentes: {}".format(self.__destinosFrecuentes))

    # Setters

    def setPropietario(self, nProp):
        self.__propietario = nProp

    def setServicios(self, nServ):      # Lista de strings? Cada string es un servicio
        self.__serviciosABordo = nServ

    def setDestinos(self, nDestinos):   # Lista de objetos tipo pais?
        self.__destinosFrecuentes = nDestinos
