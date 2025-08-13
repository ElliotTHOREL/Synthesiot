from app.connection import get_db_cursor

def get_files():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT id, name FROM fichiers")
        return cursor.fetchall()