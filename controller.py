from db import get_db

def get_puntajes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT universidad, carrera, ciudad, region, puntaje FROM puntajes"
    cursor.execute(query)
    return cursor.fetchall()
