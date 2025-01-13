from fastapi import FastAPI
from connection import *
from pydantic import BaseModel

app = FastAPI()

# metode per veure si funciona tot
@app.get("/")
def salutacio():
    return "Hola"


# Exercici 1
class Formulari(BaseModel):
    nombre: str
    apellido: str
    email: str
    descripcion: str | None = None
    curso: int
    anio: int
    direccion: str
    codi_postal: int | None = None
    password: str