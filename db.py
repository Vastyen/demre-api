import sqlite3

DATABASE_NAME = "puntajes.db"

def get_db():
    con = sqlite3.connect(DATABASE_NAME)
    return con

