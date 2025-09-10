import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normal(self):
        mag = self.magnitud()
        if mag == 0:
            return AlgebraVectorial(0, 0, 0)
        return AlgebraVectorial(self.x / mag, self.y / mag, self.z / mag)

    def escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def escalar_por_vector(self, x):
        return AlgebraVectorial(self.x * x, self.y * x, self.z * x)

    def cruz(self, otro):
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return AlgebraVectorial(cx, cy, cz)

    def perpendicular_diagonales(self, otro):
        suma = self + otro
        resta = self - otro
        return suma.magnitud() == resta.magnitud()
    
    def proyeccion(self, otro):
        proy = self.escalar(otro) / otro.escalar(otro)
        return AlgebraVectorial(otro.x * proy, otro.y * proy, otro.z * proy)

    def componente(self, otro):
        return self.escalar(otro) / otro.magnitud()

# Función para pedir vectores
def pedir_vector(nombre):
    print(f"Ingrese las coordenadas del vector {nombre}:")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    return AlgebraVectorial(x, y, z)

# Programa principal
v1 = pedir_vector("v1")
v2 = pedir_vector("v2")
x = float(input("Ingrese un escalar para multiplicar v1: "))

print("\nResultados:")
print("v1:", v1)
print("v2:", v2)
print("Magnitud de v1:", v1.magnitud())
print("Magnitud de v2:", v2.magnitud())
print("Escalar v1 · v2:", v1.escalar(v2))
print("Producto Vectorial v1 x v2:", v1.cruz(v2))
print("Normal de v1:", v1.normal())
print("Normal de v2:", v2.normal())
print("v1 * escalar:", v1.escalar_por_vector(x))
print("¿Perpendiculares por diagonales?", v1.perpendicular_diagonales(v2))
print("Proyección ortogonal de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en la dirección de v2:", v1.componente(v2)) 