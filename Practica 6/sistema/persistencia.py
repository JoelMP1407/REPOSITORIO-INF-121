# persistencia.py
import json
from clases import Biblioteca, Libro, Autor, Estudiante

ARCHIVO = "bibliotecas.json"

def guardar_bibliotecas(bibliotecas):
    data = []
    for b in bibliotecas:
        data.append({
            "nombre": b.nombre,
            "libros": [{"titulo": l.titulo, "isbn": l.isbn} for l in b.libros_disponibles],
            "autores": [{"nombre": a.nombre, "nacionalidad": a.nacionalidad} for a in b.autores_registrados],
            "prestamos": [{
                "estudiante": {"nombre": p.estudiante.nombre, "codigo": p.estudiante.codigo},
                "libro": p.libro.titulo,
                "fecha_prestamo": p.fecha_prestamo,
                "fecha_devolucion": p.fecha_devolucion
            } for p in b.prestamos_activos]
        })
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def cargar_bibliotecas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
        bibliotecas = []
        for b in data:
            biblioteca = Biblioteca(b["nombre"])
            # reconstruir libros
            for l in b["libros"]:
                biblioteca.agregar_libro(Libro(l["titulo"], l["isbn"]))
            # reconstruir autores
            for a in b["autores"]:
                biblioteca.agregar_autor(Autor(a["nombre"], a["nacionalidad"]))
            # reconstruir préstamos
            for p in b["prestamos"]:
                estudiante = Estudiante(p["estudiante"]["nombre"], p["estudiante"]["codigo"])
                # buscar libro por título
                libro = next((lib for lib in biblioteca.libros_disponibles if lib.titulo == p["libro"]), None)
                if libro:
                    biblioteca.prestar_libro(estudiante, libro, p["fecha_prestamo"], p["fecha_devolucion"])
            bibliotecas.append(biblioteca)
        return bibliotecas
    except FileNotFoundError:
        return []
