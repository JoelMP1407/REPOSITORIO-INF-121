class Biblioteca:
    class Horario:
        def __init__(self, diasDeApertura, horaDeApertura, horaDeCierre):
            self.__diasDeApertura = diasDeApertura
            self.__horaDeApertura = horaDeApertura
            self.__horaDeCierre = horaDeCierre

        def mostrarInfo(self):
            print(f"Horario de Atencion: [Dias: {self.__diasDeApertura}, Hora de Apertura: {self.__horaDeApertura}, Hora de Cierre: {self.__horaDeCierre}]")
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__librosDisponibles = []
        self.__autoresRegistrados = []
        self.__prestamosActivos = []
            
    def agregarLibro(self, libro):
        self.__librosDisponibles.append(libro)
            
    def agregarAutor(self, autor):
        self.__autoresRegistrados.append(autor)
            
    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo("5 de noviembre", "5 de diciembre", estudiante, libro)
        self.__prestamosActivos.append(prestamo)
            
    def mostrarEstado(self):
        print(f"Biblioteca: {self.__nombre}")
        print("Libros disponibles:")
        for libro in self.__librosDisponibles:
            libro.leer()
        print("Autores registrados:")
        for autor in self.__autoresRegistrados:
            autor.mostrarInfo()
        print("Préstamos activos:")
        for prestamo in self.__prestamosActivos:
            prestamo.mostrarInfo()
    def cerrarBiblioteca(self):
        print("La biblioteca está cerrada.")
        self.__prestamosActivos.clear()

class Libro:
    class Pagina:
        def __init__(self, numeroDePagina, contenido):
            self.__numeroDePagina = numeroDePagina
            self.__contenido = contenido
        def mostrarInfo(self):
            print(f"Pagina: [Nro Pagina: {self.__numeroDePagina}, Contenido: {self.__contenido}]")
    
    def __init__(self, titulo, ISBN, contenidoDePaginas):
        self.__titulo = titulo
        self.__ISBN = ISBN
        self.__Paginas = []
        nroPagina = 1
        for contenido in contenidoDePaginas:
            pagina = self.Pagina(nroPagina, contenido)
            self.__Paginas.append(pagina)
            nroPagina = nroPagina + 1

    def getTitulo(self):
        return self.__titulo
    
    def leer(self):
        print(f"Libro: {self.__titulo}, ISBN: {self.__ISBN}")
        for pagina in self.__Paginas:
            pagina.mostrarInfo()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.__nombre}, Nacionalidad: {self.__nacionalidad}")

class Estudiante:
    def __init__(self, codigoDeEstudiante, nombre):
        self.__codigoDeEstudiante = codigoDeEstudiante
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def mostrarInfo(self):
        print(f"Estudiante: {self.__nombre}, Codigo: {self.__codigoDeEstudiante}")

class Prestamo:
    def __init__(self, fechaDePrestamo, fechaDeDevolucion, refEstudiante, refLibro):
        self.__fechaDePrestamo = fechaDePrestamo
        self.__fechaDeDevolucion = fechaDeDevolucion
        self.__refEstudiante = refEstudiante
        self.__refLibro = refLibro

    def mostrarInfo(self):
        print(f"Prestamo: [Estudiante: {self.__refEstudiante.getNombre()}, Libro: {self.__refLibro.getTitulo()}, Fecha de Prestamo: {self.__fechaDePrestamo}, Fecha de Devolucion: {self.__fechaDeDevolucion}]")

biblioteca = Biblioteca("Biblioteca Municipal")
horario = Biblioteca.Horario("Lunes a Sabado", "8:00", "18:00")
biblioteca.horario = horario
estudiante = Estudiante("1886020", "Joel Mollericona")
autor = Autor("Homero", "Griego")
libro = Libro("La Iliada", "978-3-16-148410-0", ["Canto I: Canto de la cólera", "Canto II: El catálogo de las naves", "Canto III: El duelo de Paris y Menelao"])
biblioteca.agregarAutor(autor)
biblioteca.agregarLibro(libro)
biblioteca.prestarLibro(estudiante, libro)
biblioteca.mostrarEstado()
horario.mostrarInfo()
biblioteca.cerrarBiblioteca()
