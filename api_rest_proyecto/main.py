# API REST
# José Carlos Pérez Reinosa
# Imports
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Estructura de datos
peliculas = [
    {"id": 1, "titulo": "Pulp Fiction", "descripcion": "Una historia de crimen y redención en Los Ángeles.", "año": 1994, "calificacion": 8.9, "categoria": "Crimen"},
    {"id": 2, "titulo": "El Padrino", "descripcion": "La crónica de una familia mafiosa italoamericana.", "año": 1972, "calificacion": 9.2, "categoria": "Crimen"},
    {"id": 3, "titulo": "Cadena Perpetua", "descripcion": "Dos hombres condenados a cadena perpetua encuentran consuelo y redención a través de actos de decencia común.", "año": 1994, "calificacion": 9.3, "categoria": "Drama"},
    {"id": 4, "titulo": "El caballero oscuro", "descripcion": "Batman debe enfrentarse a su mayor enemigo, el Joker, quien siembra el caos en Gotham City.", "año": 2008, "calificacion": 9.0, "categoria": "Acción"},
    {"id": 5, "titulo": "Forrest Gump", "descripcion": "La vida de un hombre con un bajo coeficiente intelectual, que logra logros extraordinarios.", "año": 1994, "calificacion": 8.8, "categoria": "Drama"},
    {"id": 6, "titulo": "La lista de Schindler", "descripcion": "Un empresario alemán salva a cientos de judíos durante el Holocausto.", "año": 1993, "calificacion": 8.9, "categoria": "Historia"},
    {"id": 7, "titulo": "El Señor de los Anillos: El retorno del Rey", "descripcion": "El enfrentamiento final por la Tierra Media mientras Frodo y Sam llegan a Mordor.", "año": 2003, "calificacion": 8.9, "categoria": "Fantasia"},
    {"id": 8, "titulo": "La guerra de las galaxias: Episodio V - El Imperio contraataca", "descripcion": "Luke Skywalker y sus amigos enfrentan a Darth Vader y el Imperio Galáctico.", "año": 1980, "calificacion": 8.7, "categoria": "Ciencia ficción"},
    {"id": 9, "titulo": "Matrix", "descripcion": "Un hacker descubre la verdad sobre su realidad y su papel en la guerra contra sus controladores.", "año": 1999, "calificacion": 8.7, "categoria": "Ciencia ficción"},
    {"id": 10, "titulo": "Gladiador", "descripcion": "Un general romano convertido en esclavo busca venganza contra el emperador que traicionó a su familia.", "año": 2000, "calificacion": 8.5, "categoria": "Acción"}
]

# Instanciamos la clase FastAPI y se asigna a la variable app.
app = FastAPI()

# Agregamos un título y versión
app.title = "API REST Peliculas"
app.version = "0.0.1"

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse, tags=['home'])
def read_root():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())

# Ruta para obtener todas las peliculas
@app.get('/peliculas', tags=['peliculas'])
def obtener_peliculas():
    return peliculas

# Ruta para obtener una pelicula por su ID
@app.get('/peliculas/{id}', tags=['peliculas'])
def obtener_pelicula(id: int):
    for pelicula in peliculas:
        if pelicula['id'] == id:
            return pelicula
    return {'mensaje': 'Pelicula no encontrada'}

# Ruta para obtener las peliculas por categoria
@app.get('/peliculas/', tags=['peliculas'])
def obtener_peliculas_por_categoria(categoria: str):
    return [pelicula for pelicula in peliculas if pelicula['categoria'] == categoria]

# Ruta para agregar una nueva pelicula
@app.post('/peliculas', tags=['peliculas'])
def crear_pelicula(id: int = Body(),titulo: str = Body(), descripcion: str = Body(), año: int = Body(), calificacion: float = Body(), categoria: str = Body()):
    peliculas.append({ 
        'id': id,
        'titulo': titulo,
        'descripcion': descripcion,
        'año': año,
        'calificacion': calificacion,
        'categoria': categoria
    })
    return peliculas

# Ruta para actualizar una pelicula existente
@app.put('/peliculas/{id}', tags=['peliculas'])
def actualizar_pelicula(id: int, titulo: str = Body(), descripcion: str = Body(), año: int = Body(), calificacion: float = Body(), categoria: str = Body()):
    for pelicula in peliculas:
        if pelicula['id'] == id:
            pelicula['titulo'] = titulo
            pelicula['descripcion'] = descripcion
            pelicula['año'] = año
            pelicula['calificacion'] = calificacion
            pelicula['categoria'] = categoria
            return peliculas
    return {'mensaje': 'Pelicula no encontrada'}

# Ruta para eliminar una pelicula
@app.delete('/peliculas/{id}', tags=['peliculas'])
def eliminar_pelicula(id: int):
    for pelicula in peliculas:
        if pelicula['id'] == id:
            peliculas.remove(pelicula)
            return peliculas
    return {'mensaje': 'Pelicula no encontrada'}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)