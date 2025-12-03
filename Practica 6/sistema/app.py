# app.py
import tkinter as tk
from ventana_libro import AppLibro
from ventana_autor import AppAutor
from ventana_prestamo import AppPrestamo
from ventana_borrar_libro import AppBorrarLibro
from ventana_borrar_autor import AppBorrarAutor
import persistencia

class App(tk.Tk):
    def __init__(self, biblioteca, todas_bibliotecas):
        super().__init__()
        self.biblioteca = biblioteca   # <-- guardar primero
        self.todas_bibliotecas = todas_bibliotecas

        self.title("Biblioteca Municipal")
        self.geometry("600x400")

        # Ahora sí puedes usar self.biblioteca
        tk.Label(self, text=f"{self.biblioteca.nombre}", font=("Arial", 24)).pack(pady=10)
        tk.Label(self, text="¿Qué desea hacer hoy?").pack(pady=5)

        tk.Button(self, text="Agregar un Libro", command=self.abrir_libro).pack(pady=5)
        tk.Button(self, text="Agregar un Autor", command=self.abrir_autor).pack(pady=5)
        tk.Button(self, text="Prestar un Libro", command=self.abrir_prestamo).pack(pady=5)
        tk.Button(self, text="Mostrar Datos", command=self.mostrar_datos).pack(pady=5)
        tk.Label(self, text="Administración", font=("Arial", 14), fg="blue").pack(pady=10)
        tk.Button(self, text="Borrar Libro", command=self.borrar_libro).pack(pady=5)
        tk.Button(self, text="Borrar Autor", command=self.borrar_autor).pack(pady=5)
        tk.Button(self, text="Cerrar Biblioteca", command=self.cerrar_biblioteca).pack(pady=5)

        self.text_area = tk.Text(self, height=10, width=60)
        self.text_area.pack(pady=10)

    def abrir_libro(self):
        AppLibro(self.biblioteca, self, self.todas_bibliotecas)

    def abrir_autor(self):
        AppAutor(self.biblioteca, self, self.todas_bibliotecas)

    def abrir_prestamo(self):
        AppPrestamo(self.biblioteca, self)

    def borrar_libro(self):
        AppBorrarLibro(self.biblioteca, self, self.todas_bibliotecas)

    def borrar_autor(self):
        AppBorrarAutor(self.biblioteca, self, self.todas_bibliotecas)

    def mostrar_datos(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, self.biblioteca.mostrar_estado())

    def cerrar_biblioteca(self):
        self.biblioteca.cerrar_biblioteca()
        persistencia.guardar_bibliotecas(self.todas_bibliotecas)  # guardar cambios
        self.quit()
