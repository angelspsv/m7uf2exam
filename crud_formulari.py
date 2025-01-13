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

