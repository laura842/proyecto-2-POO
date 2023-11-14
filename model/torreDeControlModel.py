
# Definir una clase 'TorreDeControl' con atributos y metodos

class TorreDeControlModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TorreDeControlModel, cls).__new__(cls)
        return cls._instance

    # Metodo constructor
    def __init__(self):
        self.notificacion = ""
        self.puertas = []
