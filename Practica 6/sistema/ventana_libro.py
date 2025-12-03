# ventana_libro.py
import tkinter as tk
from clases import Libro
import persistencia

class AppLibro(tk.Toplevel):
    def __init__(self, biblioteca, ventana_app, todas_bibliotecas):
        super().__init__(ventana_app)
        self.title("Agregar Libro")
        self.geometry("400x300")
        self.biblioteca = biblioteca
        self.todas_bibliotecas = todas_bibliotecas

        tk.Label(self, text="Título").pack()
        self.titulo_entry = tk.Entry(self)
        self.titulo_entry.pack()

        tk.Label(self, text="ISBN").pack()
        self.isbn_entry = tk.Entry(self)
        self.isbn_entry.pack()

        tk.Button(self, text="Agregar", command=self.agregar_libro).pack(pady=10)
        tk.Button(self, text="Volver", command=self.destroy).pack()

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        isbn = self.isbn_entry.get()
        libro = Libro(titulo, isbn)
        self.biblioteca.agregar_libro(libro)
        persistencia.guardar_bibliotecas(self.todas_bibliotecas)
        tk.messagebox.showinfo("Éxito", "Libro agregado correctamente")
