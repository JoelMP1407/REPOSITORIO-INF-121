# ventana_inicio.py
import tkinter as tk
from tkinter import ttk, messagebox
from clases import Biblioteca
from app import App   # Importamos la ventana principal
import persistencia

class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Bibliotecas")
        self.geometry("500x400")

        # Lista de bibliotecas creadas
        self.bibliotecas = persistencia.cargar_bibliotecas()

        # --- Título principal ---
        tk.Label(self, text="Bienvenido al Sistema de Bibliotecas",
                 font=("Arial", 18), fg="blue").pack(pady=15)

        tk.Label(self, text="¿Qué quieres hacer hoy?", font=("Arial", 12)).pack(pady=5)

        # --- Crear nueva biblioteca ---
        tk.Label(self, text="Crear una nueva biblioteca:").pack(pady=5)
        self.nombre_entry = tk.Entry(self, width=40)
        self.nombre_entry.pack(pady=5)
        tk.Button(self, text="Crear Biblioteca", command=self.crear_biblioteca).pack(pady=5)

        # --- Acceder a biblioteca existente ---
        tk.Label(self, text="Acceder a una biblioteca o borrarla:").pack(pady=10)
        self.combo_var = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.combo_var, state="readonly", width=40)
        self.combo.pack(pady=5)
        tk.Button(self, text="Acceder", command=self.acceder_biblioteca).pack(pady=5)
        tk.Button(self, text="Borrar Biblioteca", command=self.borrar_biblioteca).pack(pady=5)


        self.actualizar_combobox()

    def crear_biblioteca(self):
        nombre = self.nombre_entry.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar un nombre para la biblioteca.")
            return
        nueva = Biblioteca(nombre)
        self.bibliotecas.append(nueva)
        persistencia.guardar_bibliotecas(self.bibliotecas)
        self.actualizar_combobox()
        messagebox.showinfo("Éxito", f"Biblioteca '{nombre}' creada correctamente.")

    def actualizar_combobox(self):
        nombres = [b.nombre for b in self.bibliotecas]
        self.combo["values"] = nombres
        if nombres:
            self.combo.current(0)

    def acceder_biblioteca(self):
        nombre = self.combo_var.get()
        if not nombre:
            messagebox.showerror("Error", "Debe seleccionar una biblioteca.")
            return
        # Buscar la biblioteca seleccionada
        for b in self.bibliotecas:
            if b.nombre == nombre:
                self.withdraw()  # Ocultamos ventana inicio
                App(b, self.bibliotecas).mainloop()
                break

    def borrar_biblioteca(self):
        nombre = self.combo_var.get()
        if not nombre:
            messagebox.showerror("Error", "Debe seleccionar una biblioteca.")
            return
        self.bibliotecas = [b for b in self.bibliotecas if b.nombre != nombre]
        persistencia.guardar_bibliotecas(self.bibliotecas)
        self.actualizar_combobox()
        messagebox.showinfo("Éxito", f"Biblioteca '{nombre}' borrada correctamente")



if __name__ == "__main__":
    VentanaInicio().mainloop()
