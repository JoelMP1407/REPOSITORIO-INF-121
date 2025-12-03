# ventana_prestamo.py
import tkinter as tk
from clases import Estudiante

class AppPrestamo(tk.Toplevel):
    def __init__(self, biblioteca, ventana_app):
        super().__init__(ventana_app)
        self.title("Realizar Préstamo")
        self.geometry("500x450")
        self.biblioteca = biblioteca
        self.ventana_app = ventana_app

        # --- Título principal ---
        tk.Label(self, text="BIBLIOTECA MUNICIPAL", font=("Arial", 20), fg="blue").pack(pady=10)
        tk.Label(self, text="Introduzca sus datos para el préstamo", font=("Arial", 12)).pack(pady=5)

        # --- Nombre estudiante ---
        tk.Label(self, text="Nombre del Estudiante").pack()
        self.nombre_entry = tk.Entry(self, width=40)
        self.nombre_entry.pack()

        # --- Código estudiante ---
        tk.Label(self, text="Código del Estudiante").pack()
        self.codigo_entry = tk.Entry(self, width=40)
        self.codigo_entry.pack()

        # --- Fecha préstamo ---
        tk.Label(self, text="Fecha de Préstamo").pack()
        self.fecha_prestamo_entry = tk.Entry(self, width=40)
        self.fecha_prestamo_entry.pack()

        # --- Fecha devolución ---
        tk.Label(self, text="Fecha de Devolución").pack()
        self.fecha_devolucion_entry = tk.Entry(self, width=40)
        self.fecha_devolucion_entry.pack()

        # --- Selección de libro ---
        tk.Label(self, text="Seleccione Libro").pack()
        self.libro_var = tk.StringVar(self)
        opciones = [libro.titulo for libro in biblioteca.libros_disponibles]

        if opciones:
            self.libro_var.set(opciones[0])  # valor inicial obligatorio
            self.libro_menu = tk.OptionMenu(self, self.libro_var, *opciones)
        else:
            self.libro_var.set("No hay libros")
            self.libro_menu = tk.OptionMenu(self, self.libro_var, "No hay libros")

        self.libro_menu.pack()

        # --- Resultado ---
        self.result_label = tk.Label(self, text="", fg="blue")
        self.result_label.pack(pady=10)

        # --- Botones ---
        tk.Button(self, text="Realizar Préstamo", command=self.realizar_prestamo).pack(pady=5)
        tk.Button(self, text="Volver", command=self.destroy).pack(pady=5)

    def realizar_prestamo(self):
        nombre = self.nombre_entry.get().strip()
        codigo = self.codigo_entry.get().strip()
        fecha_prestamo = self.fecha_prestamo_entry.get().strip()
        fecha_devolucion = self.fecha_devolucion_entry.get().strip()
        titulo = self.libro_var.get()

        # Validación de campos
        if not nombre or not codigo or not fecha_prestamo or not fecha_devolucion or not titulo:
            self.result_label.config(text="Complete todos los campos.", fg="red")
            return

        # Buscar libro
        libro_seleccionado = None
        for libro in self.biblioteca.libros_disponibles:
            if libro.titulo == titulo:
                libro_seleccionado = libro
                break

        if libro_seleccionado:
            if self.biblioteca.esta_prestado(libro_seleccionado):
                self.result_label.config(text=f"El libro '{libro_seleccionado.titulo}' ya está prestado.", fg="red")
            else:
                estudiante = Estudiante(nombre, codigo)
                self.biblioteca.prestar_libro(estudiante, libro_seleccionado, fecha_prestamo, fecha_devolucion)
                self.result_label.config(text="Préstamo realizado con éxito.", fg="green")