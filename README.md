# Sistema Básico de Gestión de Garaje 

Nombre: Pablo Alexander Ramon Mosquera

Una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. Este proyecto fue creado para aplicar y demostrar los principios de la **Programación Orientada a Objetos (POO)** 

##Características
* **Registro de vehículos:** Permite ingresar la Placa, Marca y Propietario de un vehículo.
* **Visualización:** Muestra todos los vehículos registrados en una tabla (Treeview) actualizada en tiempo real.
* **Limpieza de formulario:** Botón dedicado para vaciar los campos de entrada rápidamente.
* **Validación básica:** Evita el registro de vehículos si hay campos vacíos.

## Arquitectura del Proyecto
El código sigue un patrón de diseño basado en la separación de responsabilidades, estructurado de la siguiente manera:

* **`modelos/`**: Contiene la clase `Vehiculo` con sus atributos privados y métodos encapsulados (`@property`).
* **`servicios/`**: Contiene `GarajeServicio`, encargado de la lógica de negocio y el almacenamiento en memoria de los registros.
* **`ui/`**: Contiene `AppTkinter`, que maneja exclusivamente la interfaz gráfica y la interacción con el usuario.
* **`main.py`**: El punto de entrada que inicializa el servicio y arranca la interfaz gráfica.
