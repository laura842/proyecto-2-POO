# Definir una clase 'Aeronave' con atributos y metodos
class AeronaveModel:
    # Metodo constructor
    def __init__(self, idA, marca, modelo, capacidad, velMax, autonomia, anioFab, ubicacion):
        self.__id = idA
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__velMax = velMax
        self.__autonomia = autonomia
        self.__anioFab = anioFab
        self.__estado = "Disponible"
        self.__totalAsign = False
        self.__vuelosAsign = []
        self.__ubicacion = ubicacion

    def imprimirDatosAero(self):
        print("ID: {}".format(self.__id))
        print("Marca: {}".format(self.__marca))
        print("Modelo {}".format(self.__modelo))
        print("Capacidad de pasajeros: {}".format(self.__capacidad))
        print("Velocidad maxima: {}".format(self.__velMax))
        print("Autonomia: {}".format(self.__autonomia))
        print("Anio de fabricacion: {}".format(self.__anioFab))
        print("Estado: {}".format(self.__estado))
        """print("¿Esta totalmente asignada?; {}".format(self.totalAsign))"""
        print("Vuelos asignados: {}".format(self.__vuelosAsign))
        print("Ubicacion: {}".format(self.__ubicacion))

    # Setters

    def setMarca(self, nMarca):
        self.__marca = nMarca

    def setModelo(self, nModelo):
        self.__modelo = nModelo

    def setCapacidad(self, nCap):
        self.__capacidad = nCap

    def setVelMax(self, nVelMax):
        self.__velMax = nVelMax

    def setAutonomia(self, nAuto):
        self.__autonomia = nAuto

    def setAnioFab(self, nAnio):
        self.__anioFab = nAnio

    def setEstado(self, nEstado):
        self.__estado = nEstado

    # Getters

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getCapacidad(self):
        return self.__capacidad

    def getVelMax(self):
        return self.__velMax

    def getAutonomia(self):
        return self.__autonomia

    def getAnioFab(self):
        return self.__anioFab

    def getEstado(self):
        return self.__estado

    # Otros

    def anadirVuelo(self, nuevoVuelo):
        if self.__totalAsign or self.__estado == "En mantenimiento":
            print("La nave ya tiene 3 vuelos asignados, no es posible asignar más vuelos")

        else:
            if nuevoVuelo.origen == "CLO":
                flag = False

                for i in self.__vuelosAsign:
                    if self.__vuelosAsign[i].origen == "CLO":
                        flag = True

                if flag:
                    print("La nave ya tiene un vuelo con origen en la ciudad de Cali")

                elif not flag and self.__estado != "En aeropuerto":
                    print("La aeronave no esta en el aeropuerto, no se puede asignar vuelo con origen en Cali")

                elif not flag and self.__estado == "En aeropuerto":
                    self.__vuelosAsign.append(nuevoVuelo)
                    print("Vuelo asignado correctamente")
                    if self.__vuelosAsign == 3:
                        self.__totalAsign = True

            elif nuevoVuelo.origen != "CLO":  # Manejo excepciones por si se intenta agregar algo que no sea tipo vuelo
                self.__vuelosAsign.append(nuevoVuelo)
                print("Vuelo asignado correctamente")
                if self.__vuelosAsign == 3:
                    self.__totalAsign = True

            else:
                print("Intente de nuevo")


"""
    def reportarUb(self):
        print("Hola, hay que arreglar esto")
    
    def despegar(self):
        print("D")

    def aterrizar(self):
        print("A")
        
    def recibido(self):
        print("R")
"""
