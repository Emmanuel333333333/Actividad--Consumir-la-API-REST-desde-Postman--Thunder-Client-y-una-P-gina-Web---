from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/projects")
def get_projects():
    return projects

# Permitir acceso desde HTML/JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos simulados
projects = [
    {"id": 1, "nombre": "Proyecto ADSO", "descripcion": "Plataforma educativa en FastAPI"},
    {"id": 2, "nombre": "Tienda Online", "descripcion": "E-commerce con React y Node"},
    {"id": 3, "nombre": "Gestor de tareas", "descripcion": "App de productividad"}
]

