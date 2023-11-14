# This is a sample Python script.
import streamlit as st

from model.avionModel import AvionModel
from model.pasajeroModel import PasajeroModel
from model.torreDeControlModel import TorreDeControlModel
from model.tripulacionModel import TripulacionModel
from model.puertaDeEmbarqueModel import PuertaDeEmbarqueModel

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

miPasajero = PasajeroModel("Juan", "Amaya", "1001349877", "12/03/2001", "H",
                      "Barlovento", "3184515242", "ninolindo@gmail.com", "rolo",
                      2, "alergia y muy lindo")

# Pasajero.imprimirDatosPas(miPasajero)

miTripulacion = TripulacionModel("Laura", "Lozano", "1006017232", "10/09/2003",
                            "M", "Las Lajas", "3137293923", "lauloz@gmail.com", "piloto",
                            1, 4)

# Tripulacion.imprimirDatosTrip(miTripulacion)

miAvion = AvionModel("AV01", "Boeing", "Airbus320", 320, 40000, 200000,
                2014, False, "", 100000, 6, "Comercial")

AvionModel.imprimirDatosAv(miAvion)

puertaN = PuertaDeEmbarqueModel("1", "Sur", True, "", "hola")

s1 = TorreDeControlModel()
s2 = TorreDeControlModel()

"""
if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")

print(s1.notificacion)
print(s2.notificacion)
print(s1)
print(s2)
"""
