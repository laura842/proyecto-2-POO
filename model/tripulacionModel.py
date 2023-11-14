from personaModel import PersonaModel


# Definir una clase 'Tripulacion' con atributos y metodos
class TripulacionModel(PersonaModel):
    # Metodo constructor
    def __init__(self, nombre, apellido, cedula, fechaNacimiento, genero, direccion, telefono, correo, cargo, aniosExp,
                 maxHorasDiarias):
        super().__init__(nombre, apellido, cedula, fechaNacimiento, genero, direccion, telefono, correo)
        self.cargo = cargo
        self.aniosExp = aniosExp
        self.maxHorasDiarias = maxHorasDiarias

    def imprimirDatosTrip(self):
        super().imprimirDatosPer()
        print("Puesto: {}".format(self.cargo))
        print("Anios de experiencia: {}".format(self.aniosExp))
        print("Maximo de horas de trabajo diarias: {}".format(self.maxHorasDiarias))
