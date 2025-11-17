class Persona:
    def __init__(self, nombre: str, edad: int, peso: float):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getPeso(self):
        return self.__peso


class Cabina:
    def __init__(self, nroCab: int):
        self.__nroCab = nroCab
        self.__personasABordo = []

    def getNroCab(self):
        return self.__nroCab

    def getPersonasABordo(self):
        return self.__personasABordo

    def agregarPersona(self, p: Persona):
        pesoTotal = sum(persona.getPeso() for persona in self.__personasABordo)
        if pesoTotal + p.getPeso() <= 850 and len(self.__personasABordo) < 10:
            self.__personasABordo.append(p)
        else:
            print("No se puede agregar más personas, límite alcanzado")

    def verificarCabina(self):
        pesoTotal = sum(persona.getPeso() for persona in self.__personasABordo)
        if len(self.__personasABordo) <= 10 and pesoTotal <= 850:
            print(f"La cabina [{self.getNroCab()}] cumple con las reglas establecidas")
        else:
            print(f"La cabina [{self.getNroCab()}] NO cumple con las reglas establecidas")


class Linea:
    def __init__(self, color: str):
        self.__color = color
        self.__filaPersonas = []
        self.__cabinas = []
        self.__cantidadCabinas = 0

    def getColor(self):
        return self.__color

    def agregarPersona(self, p: Persona):
        self.__filaPersonas.append(p)

    def agregarCabina(self, cabina: Cabina):
        self.__cabinas.append(cabina)
        self.__cantidadCabinas = self.__cantidadCabinas + 1

    def subirPersonaACabina(self, p: Persona, cabina: Cabina):
        if p in self.__filaPersonas:
            if len(cabina.getPersonasABordo()) < 10:
                cabina.agregarPersona(p)
                self.__filaPersonas.remove(p)
            else:
                print("La cabina está llena.")

    def pagarPasaje(self):
        total = 0
        for c in self.__cabinas:
            for p in c.getPersonasABordo():
                if p.getEdad() <= 25 or p.getEdad() >= 60:
                    total += 1.5
                else:
                    total += 3.0
        return total

    def calcularPasajeTotalRegular(self):
        totalRegular = 0
        for c in self.__cabinas:
            for p in c.getPersonasABordo():
                if 25 < p.getEdad() < 60:
                    totalRegular += 3.0
        return totalRegular


class MiTeleferico:
    def __init__(self):
        self.__lineas = []

    def agregarLinea(self, linea: Linea):
        self.__lineas.append(linea)
        
    def agregarPersonaFila(self, p: Persona, linea: Linea):
        linea.append(p)
        
    def agregarCabina(self, linea: Linea):
        self.__lineas.append(linea)

    def ingresoTotal(self):
        total = 0
        for linea in self.__lineas:
            total = total + linea.pagarPasaje()
        return total

    def lineaConMasIngresosDeTarifaRegular(self):
        IngresoMayor = 0
        for linea in self.__lineas:
            if linea.calcularPasajeTotalRegular() > IngresoMayor:
                IngresoMayor = linea.calcularPasajeTotalRegular()
                mayor = linea
        return mayor.getColor()

##Creacion de objetos     
teleferico = MiTeleferico()

lineaRoja = Linea("Roja")
lineaAmarilla = Linea("Amarilla")
lineaVerde = Linea("Verde")

teleferico.agregarLinea(lineaRoja)
teleferico.agregarLinea(lineaAmarilla)
teleferico.agregarLinea(lineaVerde)

##Llenado de cabinas
cab1 = Cabina(1)
cab2 = Cabina(2)
cab3 = Cabina(3)
cab4 = Cabina(4)
cab5 = Cabina(5)
cab6 = Cabina(6)
cab7 = Cabina(7)
cab8 = Cabina(8)
cab9 = Cabina(9)
lineaRoja.agregarCabina(cab1)
lineaRoja.agregarCabina(cab2)
lineaRoja.agregarCabina(cab3)
lineaAmarilla.agregarCabina(cab4)
lineaAmarilla.agregarCabina(cab5)
lineaAmarilla.agregarCabina(cab6)
lineaVerde.agregarCabina(cab7)
lineaVerde.agregarCabina(cab8)
lineaVerde.agregarCabina(cab9)

##Creamos personas
p1 = Persona("Juan", 17, 56.0)
p2 = Persona("Maria", 62, 46.5)
p3 = Persona("Pepe", 45, 62.3)
p4 = Persona("Ana", 7, 34.5)
p5 = Persona("Carlos", 34, 42.2)
p6 = Persona("Luisa", 29, 58.1)
p7 = Persona("Miguel", 15, 70.0)
p8 = Persona("Sofia", 66, 48.3)
p9 = Persona("Diego", 50, 80.5)

##Que las personas hagan fila en las lineas
lineaRoja.agregarPersona(p1)
lineaRoja.agregarPersona(p2)
lineaRoja.agregarPersona(p3)
lineaAmarilla.agregarPersona(p4)
lineaAmarilla.agregarPersona(p5)
lineaAmarilla.agregarPersona(p6)
lineaVerde.agregarPersona(p7)
lineaVerde.agregarPersona(p8)
lineaVerde.agregarPersona(p9)

##Subir personas a las cabinas
lineaRoja.subirPersonaACabina(p1, cab1)
lineaRoja.subirPersonaACabina(p2, cab1)
lineaRoja.subirPersonaACabina(p3, cab2)
lineaAmarilla.subirPersonaACabina(p4, cab4)
lineaAmarilla.subirPersonaACabina(p5, cab4)
lineaAmarilla.subirPersonaACabina(p6, cab5)
lineaVerde.subirPersonaACabina(p7, cab7)
lineaVerde.subirPersonaACabina(p8, cab7)
lineaVerde.subirPersonaACabina(p9, cab8)

##Verificar si las reglas se cumplen
cab1.verificarCabina()
cab2.verificarCabina()
cab3.verificarCabina()
cab4.verificarCabina()
cab5.verificarCabina()
cab6.verificarCabina()
cab7.verificarCabina()
cab8.verificarCabina()
cab9.verificarCabina()

##Calcular ingresos
totalIngresos = teleferico.ingresoTotal()
print("El ingreso total del teleférico es:", totalIngresos)
mostraLineaMayorIngreso = teleferico.lineaConMasIngresosDeTarifaRegular()
print("La línea con mayor ingreso por tarifa regular es:", mostraLineaMayorIngreso)