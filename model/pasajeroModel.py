from personaModel import PersonaModel


# Definir una subclase 'Pasajero' que hereda de 'Persona'
class PasajeroModel(PersonaModel):
    # Metodo constructor
    def __init__(self, nombre, apellido, cedula, fechaNacimiento, genero, direccion, telefono, correo, nacionalidad,
                 maletas, infoMedica):
        super().__init__(nombre, apellido, cedula, fechaNacimiento, genero, direccion, telefono, correo)
        self.nacionalidad = nacionalidad
        self.maletas = maletas
        self.infoMedica = infoMedica

    def imprimirDatosPas(self):
        super().imprimirDatosPer()
        print("Nacionalidad: {}".format(self.nacionalidad))
        print("Maletas: {}".format(self.maletas))
        print("Informacion medica: {}".format(self.infoMedica))
