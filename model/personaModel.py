
# Definir una clase 'Persona' con atributos y metodos
class PersonaModel:
    # Metodo constructor
    def __init__(self, nombre, apellido, cedula, fechaNacimiento, genero, direccion, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def imprimirDatosPer(self):
        print("Nombre: {}".format(self.nombre))
        print("Apellido: {}".format(self.apellido))
        print("Cedula: {}".format(self.cedula))
        print("Fecha de nacimiento: {}".format(self.fechaNacimiento))
        print("Genero: {}".format(self.genero))
        print("Direccion: {}".format(self.direccion))
        print("Telefono: {}".format(self.telefono))
        print("Correo: {}".format(self.correo))
