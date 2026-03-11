class Vehiculo:
    #Clase que representa un vehículo en el garaje.
    
    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
    return (
        f"Placa: {self.placa} | "
        f"Marca: {self.marca} | "
        f"Propietario: {self.propietario}"
    )