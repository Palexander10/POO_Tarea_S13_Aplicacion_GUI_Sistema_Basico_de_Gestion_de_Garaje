from modelos.vehiculo import Vehiculo

class GarajeServicio:
    #Clase que maneja la lógica de registro de los vehículos.
    
    def __init__(self):
        self.vehiculos = [] # Lista para almacenar los objetos Vehiculo

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self.vehiculos