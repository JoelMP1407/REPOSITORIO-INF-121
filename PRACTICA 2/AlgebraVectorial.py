import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):  # Sobrecarga de constructor
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, otro):  # Suma de vectores
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):  # Resta de vectores
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def escalar(self, otro):  # Producto punto
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def magnitud(self):  # Magnitud del vector
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def perpendicular_sumyres(self, otro):
        # Método a) |a + b| == |a - b|
        sum_mag = (self + otro).magnitud()
        diff_mag = (self - otro).magnitud()
        return sum_mag == diff_mag

    def perpendicular_escalar(self, otro):
        # Método b) a · b == 0
        return self.escalar(otro)==0.0
    
    def perpendicular_simetrica(self, otro):
        # Método c) |a - b| == |b - a|
        resta1 = self - otro
        resta2 = otro - self
        return resta1.magnitud() == resta2.magnitud()
    
    def perpendicular_por_magnitudes(self, otro):
        # Método d) |a + b|² == |a|² + |b|²
        suma = self + otro
        izquierda = suma.magnitud() ** 2
        derecha = self.magnitud() ** 2 + otro.magnitud() ** 2
        return izquierda == derecha

    def paralelos(self, otro):
        # Método e) a = k * b
        if otro.x != 0:
            k = self.x / otro.x
            return (self.y == k * otro.y) and (self.z == k * otro.z)
        elif otro.y != 0:
            k = self.y / otro.y
            return (self.x == k * otro.x) and (self.z == k * otro.z)
        elif otro.z != 0:
            k = self.z / otro.z
            return (self.x == k * otro.x) and (self.y == k * otro.y)
        else:
            return self.x == 0 and self.y == 0 and self.z == 0
        
    def paralelos_por_magnitudes(self, otro):
        # Método f) a x b = 0
        cross_x = self.y * otro.z - self.z * otro.y 
        cross_y = self.z * otro.x - self.x * otro.z
        cross_z = self.x * otro.y - self.y * otro.x
        return cross_x == 0 and cross_y == 0 and cross_z == 0

    def proyeccion(self, otro):
        # Método g) Proyₐ_b = (a · b / b · b) b
        proy = self.escalar(otro) / otro.escalar(otro)
        return AlgebraVectorial(otro.x * proy, otro.y * proy, otro.z * proy)

    def componente(self, otro):
        # Método h) Compₐ_b = (a · b / |b|)
        return self.escalar(otro) / otro.magnitud()

# Función para pedir vectores al usuario
def pedir_vector(nombre):
    print(f"Ingrese las coordenadas del vector {nombre}:")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    return AlgebraVectorial(x, y, z)

# Programa principal
v1 = pedir_vector("v1")
v2 = pedir_vector("v2")

print("\nResultados:")
print("v1:", v1)
print("v2:", v2)
print("¿Perpendiculares (por magnitudes)?", v1.perpendicular_sumyres(v2))
print("¿Perpendiculares (por producto punto)?", v1.perpendicular_escalar(v2))
print("¿Perpendiculares (simétrica)?", v1.perpendicular_simetrica(v2))
print("¿Perpendiculares (por magnitudes 2)?", v1.perpendicular_por_magnitudes(v2))
print("¿Paralelos?", v1.paralelos(v2))
print("¿Paralelos (por magnitudes)?", v1.paralelos_por_magnitudes(v2))
print("Proyección ortogonal de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en la dirección de v2:", v1.componente(v2))