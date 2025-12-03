# ventana_borrar_autor.py
import tkinter as tk
from tkinter import messagebox
import persistencia

class AppBorrarAutor(tk.Toplevel):
    def __init__(self, biblioteca, ventana_app, todas_bibliotecas):
        super().__init__(ventana_app)
        self.biblioteca = biblioteca
        self.todas_bibliotecas = todas_bibliotecas

        self.title("Borrar Autor")
        self.geometry("400x300")

        tk.Label(self, text="Seleccione un autor para borrar").pack(pady=10)

        self.autor_var = tk.StringVar(self)
        opciones = [autor.nombre for autor in biblioteca.autores_registrados]

        if opciones:
            self.autor_var.set(opciones[0])  # valor inicial obligatorio
            self.combo = tk.OptionMenu(self, self.autor_var, *opciones)
            self.combo.pack(pady=10)
            tk.Button(self, text="Borrar", command=self.borrar_autor).pack(pady=10)
        else:
            self.autor_var.set("No hay autores disponibles")
            self.combo = tk.OptionMenu(self, self.autor_var, "No hay autores disponibles")
            self.combo.pack(pady=10)
            tk.Label(self, text="No hay autores para borrar.", fg="red").pack(pady=10)

        tk.Button(self, text="Volver", command=self.destroy).pack()

    def borrar_autor(self):
        nombre = self.autor_var.get()
        if nombre == "No hay autores disponibles":
            messagebox.showerror("Error", "No hay autores para borrar.")
            return

        self.biblioteca.autores_registrados = [
            a for a in self.biblioteca.autores_registrados if a.nombre != nombre
        ]
        persistencia.guardar_bibliotecas(self.todas_bibliotecas)
        messagebox.showinfo("Éxito", f"Autor '{nombre}' borrado correctamente")
        self.destroy()
