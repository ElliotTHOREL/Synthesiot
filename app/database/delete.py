from app.connection import get_db_cursor
from app.database.create import init_bdd

def delete_file_in_bdd(id_file: int):
    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM fichiers WHERE id = %s", (id_file,))

def reset_bdd():
    with get_db_cursor() as cursor:
        cursor.execute("""
        DROP TABLE message;
        """)
        cursor.execute("""
        DROP TABLE historique;
        """)
        cursor.execute("""
        DROP TABLE chunk_agents;
        """)
        cursor.execute("""
        DROP TABLE lieutenant_agents;
        """)
        cursor.execute("""
        DROP TABLE MCP;
        """)
        cursor.execute("""
        DROP TABLE fichiers;
        """)
    init_bdd()
