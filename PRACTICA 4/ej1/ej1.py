from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def CalcularSalarioMensual(self):
        pass

    def __str__(self):
        return (f"Empleado: {self.nombre}")
    
class EmpleadoCompleto(Empleado):
    def __init__ (self, nombre, salarioAnual):
        super().__init__(nombre)
        self.salarioAnual = salarioAnual

    def CalcularSalarioMensual(self):
        return self.salarioAnual / 12
    
    def __str__(self):
        return (f"{super().__str__()}, Salario Anual: {self.salarioAnual}, Salario Mensual: {self.CalcularSalarioMensual()}")
    
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre, horasTrabajadas, tarifaPorHora):
        super().__init__(nombre)
        self.horasTrabajadas = horasTrabajadas
        self.tarifaPorHora = tarifaPorHora

    def CalcularSalarioMensual(self):
        return (self.horasTrabajadas * self.tarifaPorHora)
    
    def __str__(self):
        return (f"{super().__str__()}, Horas Trabajadas: {self.horasTrabajadas}, Tarifa por Hora: {self.tarifaPorHora}, Salario Mensual: {self.CalcularSalarioMensual()}")

Empleado = [None]*5
print("Ahora introduzca los datos de 5 empleados, 3 de tiempo completo y 2 de tiempo horario:")
print("Empleados de tiempo completo:")
for i in range(3):
    Empleado[i] = EmpleadoCompleto(input("Nombre: "), float(input("Salario Anual: ")))
    i = i + 1
print("Empleados de tiempo horario:")
for i in range(3,5):
    Empleado[i] = EmpleadoTiempoHorario(input("Nombre: "), float(input("Horas Trabajadas: ")), float(input("Tarifa por Hora: ")))
    i = i + 1

print("\nLos datos de los empleados son:")
for i in range(5):
    print(Empleado[i])
    i = i + 1