# Llamamos la libreria FastApi
from fastapi import Body, FastAPI # type: ignore
from fastapi.responses import HTMLResponse

estudiantes = [
    {"id":1,"nombre":"Juan Pérez","edad":21,"carrera":"Ingeniería Informática","promedio":8.5},
    {"id":2,"nombre":"María Gómez","edad":22,"carrera":"Derecho","promedio":9.2},
    {"id":3,"nombre":"Luis Fernández","edad":20,"carrera":"Medicina","promedio":7.8},
    {"id":4,"nombre":"Ana Martínez","edad":23,"carrera":"Arquitectura","promedio":8.9},
    {"id":5,"nombre":"Carlos Sánchez","edad":21,"carrera":"Economía","promedio":8.3}
]

# instanciamos la clase FastAPI y se asigna a la variable app.
app = FastAPI()

# Agregamos un titulo y version
app.title = 'Mi primera app con FastAPI'
app.version = '0.0.1'

# Indice que esta funcion manejara las solicitudes GET que se realicen a la URL raiz del servidor.
@app.get('/', tags=['home']) # Los tags nos permiten agrupar las rutas de la aplicacion
def message():
    return HTMLResponse(
        '''
        <h1>Bienvenidos</h1>
        <p>API de gestion de estudiantes</p>
        '''
    )

# Ruta para obtener todos los estudiantes
@app.get('/estudiantes', tags=['estudiantes'])
def obtener_estudiantes():
    return estudiantes

# Ruta para obtener un estudiante por su ID
@app.get('/estudiantes/{id}', tags=['estudiantes'])
def obtener_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            return estudiante
    return {'mensaje': 'Estudiante no encontrado'}

# Ruta para obtener estudiante por carrera
@app.get('/estudiantes/', tags=['estudiantes'])
def obtener_estudiante_por_carrera(carrera: str):
    return [estudiante for estudiante in estudiantes if estudiante['carrera'] == carrera]

# Ruta para insertar un nuevo estudiante
@app.post('/estudiantes', tags=['estudiantes'])
def crear_estudiante(id: int = Body(), nombre: str = Body(), edad: int = Body(), carrera: str = Body(), promedio: float = Body()):
    estudiantes.append({ 
        'id': id,
        'nombre': nombre,
        'edad': edad,
        'carrera': carrera,
        'promedio': promedio
    })
    return estudiantes

# Ruta para actualizar un estudiante existente
@app.put('/estudiantes/{id}', tags=['estudiantes'])
def actualizar_estudiante(id: int, nombre: str = Body(), edad: int = Body(), carrera: str = Body(), promedio: float = Body()):
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            estudiante['nombre'] = nombre
            estudiante['edad'] = edad
            estudiante['carrera'] = carrera
            estudiante['promedio'] = promedio
            return estudiantes
    return {'mensaje': 'Estudiante no encontrado'}

# Ruta para eliminar un estudiante
@app.delete('/estudiantes/{id}', tags=['estudiantes'])
def eliminar_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            estudiantes.remove(estudiante)
            return estudiantes
    return {'mensaje': 'Estudiante no encontrado'}