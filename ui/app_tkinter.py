import tkinter as tk
from tkinter import messagebox, ttk
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio

class AppTkinter:
    """Clase que maneja la interfaz gráfica de usuario (GUI)."""
    
    def __init__(self, root, servicio: GarajeServicio):
        self.root = root
        self.servicio = servicio
        
        # Configuración de la ventana principal
        self.root.title("Sistema Básico de Gestión de Garaje")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        # Variables de control para los campos de texto
        self.placa_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.propietario_var = tk.StringVar()

        self._crear_widgets()

    def _crear_widgets(self):
        # Frame para el formulario
        frame_form = tk.LabelFrame(self.root, text="Datos del Vehículo", padx=10, pady=10)
        frame_form.pack(padx=15, pady=15, fill="x")

        # Etiquetas y Entradas
        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Entry(frame_form, textvariable=self.placa_var, width=30).grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Entry(frame_form, textvariable=self.marca_var, width=30).grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Entry(frame_form, textvariable=self.propietario_var, width=30).grid(row=2, column=1, pady=5, padx=5)

        # Frame para los botones
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=2, pady=15)

        tk.Button(frame_botones, text="Agregar vehículo", bg="#4CAF50", fg="white", 
                  command=self.agregar_vehiculo).pack(side="left", padx=10)
        tk.Button(frame_botones, text="Limpiar", bg="#f44336", fg="white", 
                  command=self.limpiar_campos).pack(side="left", padx=10)

        # Tabla (Treeview) para mostrar los registros
        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(padx=15, pady=5, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_tabla, columns=("Placa", "Marca", "Propietario"), show="headings")
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Propietario", text="Propietario")
        
        self.tree.column("Placa", width=100)
        self.tree.column("Marca", width=150)
        self.tree.column("Propietario", width=200)
        
        self.tree.pack(fill="both", expand=True)

    def agregar_vehiculo(self):
        # Obtener los datos y eliminar espacios en blanco a los extremos
        placa = self.placa_var.get().strip()
        marca = self.marca_var.get().strip()
        propietario = self.propietario_var.get().strip()

        # Validación básica
        if not placa or not marca or not propietario:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos del formulario.")
            return

        # Crear el objeto y enviarlo al servicio
        nuevo_vehiculo = Vehiculo(placa, marca, propietario)
        self.servicio.agregar_vehiculo(nuevo_vehiculo)
        
        # Actualizar la vista
        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Éxito", "El vehículo se ha registrado correctamente.")

    def limpiar_campos(self):
        self.placa_var.set("")
        self.marca_var.set("")
        self.propietario_var.set("")

    def actualizar_tabla(self):
        # Limpiar la tabla antes de volver a llenarla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Iterar sobre los vehículos guardados en el servicio e insertarlos
        for v in self.servicio.obtener_vehiculos():
            self.tree.insert("", "end", values=(v.placa, v.marca, v.propietario))