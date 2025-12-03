# ventana_borrar_libro.py
import tkinter as tk
from tkinter import messagebox
import persistencia

class AppBorrarLibro(tk.Toplevel):
    def __init__(self, biblioteca, ventana_app, todas_bibliotecas):
        super().__init__(ventana_app)
        self.biblioteca = biblioteca
        self.todas_bibliotecas = todas_bibliotecas

        self.title("Borrar Libro")
        self.geometry("400x300")

        tk.Label(self, text="Seleccione un libro para borrar").pack(pady=10)

        self.libro_var = tk.StringVar(self)
        opciones = [libro.titulo for libro in biblioteca.libros_disponibles]

        if opciones:
            self.libro_var.set(opciones[0])  # valor inicial obligatorio
            self.combo = tk.OptionMenu(self, self.libro_var, *opciones)
            self.combo.pack(pady=10)
            tk.Button(self, text="Borrar", command=self.borrar_libro).pack(pady=10)
        else:
            self.libro_var.set("No hay libros disponibles")
            self.combo = tk.OptionMenu(self, self.libro_var, "No hay libros disponibles")
            self.combo.pack(pady=10)
            tk.Label(self, text="No hay libros para borrar.", fg="red").pack(pady=10)

        tk.Button(self, text="Volver", command=self.destroy).pack()

    def borrar_libro(self):
        titulo = self.libro_var.get()
        if titulo == "No hay libros disponibles":
            messagebox.showerror("Error", "No hay libros para borrar.")
            return

        self.biblioteca.libros_disponibles = [
            l for l in self.biblioteca.libros_disponibles if l.titulo != titulo
        ]
        persistencia.guardar_bibliotecas(self.todas_bibliotecas)
        messagebox.showinfo("Éxito", f"Libro '{titulo}' borrado correctamente")
        self.destroy()
