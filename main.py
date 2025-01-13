from fastapi import FastAPI
from connection import *
from pydantic import BaseModel
from crud_formulari import *

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


# Exercici 2
# post de un nou usuari
@app.post("/formulari/insert/", response_model=dict)
async def add_user(formulari: Formulari):
    resposta = insert_formulari(formulari)
    return resposta


# Exercici 4
# get de un usuari, retorna les dades del usuari en format json
@app.get("/usuari/dades/{mail}", response_model=dict)
async def llegir_dades_usuari(mail: str):
    resposta = read_user(mail)
    return schema_user(resposta)