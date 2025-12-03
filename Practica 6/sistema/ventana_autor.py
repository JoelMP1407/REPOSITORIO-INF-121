# ventana_autor.py
import tkinter as tk
from clases import Autor
import persistencia

class AppAutor(tk.Toplevel):
    def __init__(self, biblioteca, ventana_app, todas_bibliotecas):
        super().__init__(ventana_app)
        self.title("Registrar Autor")
        self.geometry("400x300")
        self.biblioteca = biblioteca
        self.todas_bibliotecas = todas_bibliotecas

        tk.Label(self, text="Nombre").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        tk.Label(self, text="Nacionalidad").pack()
        self.nacionalidad_entry = tk.Entry(self)
        self.nacionalidad_entry.pack()

        tk.Button(self, text="Registrar", command=self.registrar_autor).pack(pady=10)
        tk.Button(self, text="Volver", command=self.destroy).pack()

    def registrar_autor(self):
        nombre = self.nombre_entry.get()
        nacionalidad = self.nacionalidad_entry.get()
        autor = Autor(nombre, nacionalidad)
        self.biblioteca.agregar_autor(autor)
        persistencia.guardar_bibliotecas(self.todas_bibliotecas)
        tk.messagebox.showinfo("Éxito", "Autor registrado correctamente")
