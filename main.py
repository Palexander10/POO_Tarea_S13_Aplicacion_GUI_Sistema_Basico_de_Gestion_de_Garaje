import tkinter as tk
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter

def main():
    # 1. Instanciar el servicio (Lógica del programa)
    servicio = GarajeServicio()
    
    # 2. Configurar la ventana raíz de Tkinter
    root = tk.Tk()
    
    # 3. Iniciar la interfaz gráfica pasándole el servicio
    app = AppTkinter(root, servicio)
    
    # 4. Mantener la ventana abierta
    root.mainloop()

if __name__ == "__main__":
    main()