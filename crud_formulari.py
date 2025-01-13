from fastapi import HTTPException

from connection import *

def insert_formulari(formulari):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #preparem la query insert per la taula
        cur.execute("INSERT INTO formulari (nombre, apellido, email, descripcion, curso, anio, direccion, codi_postal, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (formulari.nombre, formulari.apellido, formulari.email, formulari.descripcion, formulari.curso, formulari.anio, formulari.direccion, formulari.codi_postal, formulari.password))

        #desem els canvis a la taula
        conn.commit()

        return {"message": "nou registre fet amb exit"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()


# funcio schema per exercici 3
def schema_user(lista) -> dict:
    return {
        "name": lista[0],
        "surname": lista[1],
        # el password es un camp sensible
        "email": lista[3],
        "address": lista[4],
        "cp": lista[5],
        "age": lista[7]
    }


# exercici 4
def read_user(mail):
    try:
        conn = connection_db()
        cur = conn.cursor()

        #preparem query select de un usuari segons el seu email
        cur.execute("SELECT * FROM usuarios WHERE email = %s", (mail,))

        #rebem resultat query_select
        result_sql = cur.fetchone()

        #si no existeix email, execpcio
        if result_sql is None:
            raise HTTPException(status_code=404, detail="Main no trobat")

        #retornem les dades del usuari en una llista
        return result_sql
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error amb la bbdd. {str(e)}')
    finally:
        cur.close()
        conn.close()
