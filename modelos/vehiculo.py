class Vehiculo:
    #Clase que representa un vehículo en el garaje.
    
    def __init__(self, placa, marca, propietario):
        # Al asignar sin el guion bajo aquí, Python llama automáticamente a los setters
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    # --- GETTERS Y SETTERS PARA 'PLACA' ---
    @property
    def placa(self):
        """Getter para obtener la placa."""
        return self._placa
        
    @placa.setter
    def placa(self, valor):
        """Setter para asignar la placa."""
        self._placa = valor

    # --- GETTERS Y SETTERS PARA 'MARCA' ---
    @property
    def marca(self):
        """Getter para obtener la marca."""
        return self._marca
        
    @marca.setter
    def marca(self, valor):
        """Setter para asignar la marca."""
        self._marca = valor

    # --- GETTERS Y SETTERS PARA 'PROPIETARIO' ---
    @property
    def propietario(self):
        """Getter para obtener el propietario."""
        return self._propietario
        
    @propietario.setter
    def propietario(self, valor):
        """Setter para asignar el propietario."""
        self._propietario = valor

    def __str__(self):
        return (
            f"Placa: {self.placa} | "
            f"Marca: {self.marca} | "
            f"Propietario: {self.propietario}"
        )