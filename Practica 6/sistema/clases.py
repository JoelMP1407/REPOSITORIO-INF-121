# clases.py
class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo}, ISBN: {self.isbn}"


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}"


class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Estudiante: {self.nombre}, Código: {self.codigo}"


class Prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, estudiante, libro):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estudiante = estudiante
        self.libro = libro

    def __str__(self):
        return f"Préstamo: {self.estudiante.nombre}, Libro: {self.libro.titulo}, " \
               f"Prestado: {self.fecha_prestamo}, Devolución: {self.fecha_devolucion}"
    

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []
        self.autores_registrados = []
        self.prestamos_activos = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def agregar_autor(self, autor):
        self.autores_registrados.append(autor)

    def prestar_libro(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        for p in self.prestamos_activos:
            if p.libro == libro:
                print(f"El libro {libro.titulo} ya está prestado.")
                return
        prestamo = Prestamo(fecha_prestamo, fecha_devolucion, estudiante, libro)
        self.prestamos_activos.append(prestamo)

    def esta_prestado(self, libro):
        return any(p.libro == libro for p in self.prestamos_activos)

    def mostrar_estado(self):
        estado = f"Biblioteca: {self.nombre}\n"
        estado += "Libros disponibles:\n"
        for libro in self.libros_disponibles:
            estado += f" - {libro}\n"
        estado += "Autores registrados:\n"
        for autor in self.autores_registrados:
            estado += f" - {autor}\n"
        estado += "Préstamos activos:\n"
        for prestamo in self.prestamos_activos:
            estado += f" - {prestamo}\n"
        return estado

    def cerrar_biblioteca(self):
        print("La biblioteca está cerrada.")
        # Solo limpiar préstamos, mantener libros y autores
        self.prestamos_activos.clear()