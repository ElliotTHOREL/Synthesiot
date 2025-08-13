from app.connection import get_db_cursor

def init_bdd():
    with get_db_cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fichiers(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            texte MEDIUMTEXT,
            hash_normalise CHAR(64),
            INDEX idx_hash_normalise (hash_normalise)
        )
        """)

        # MCP table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS MCP(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_fichier INT,
            nb_chunk_agents INT,
            nb_lieutenant_agents INT,
            FOREIGN KEY (id_fichier) REFERENCES fichiers(id) ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunk_agents(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_mcp INT,
            position INT,
            texte TEXT,
            contexte TEXT,
            summary TEXT,
            FOREIGN KEY (id_mcp) REFERENCES MCP(id) ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_chunk_agent INT,
            FOREIGN KEY (id_chunk_agent) REFERENCES chunk_agents(id) ON DELETE CASCADE
        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS message(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_historique INT,
            numero_message INT,
            auteur VARCHAR(255),
            content TEXT,
            FOREIGN KEY (id_historique) REFERENCES historique(id) ON DELETE CASCADE
        )
        """)



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lieutenant_agents(
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_mcp INT,
                id_first_sub_agent INT,
                id_last_sub_agent INT,
                state_orchestrateur TINYINT,   
                summary TEXT,
                position INT,
                FOREIGN KEY (id_mcp) REFERENCES MCP(id) ON DELETE CASCADE
            )
            """
        )
        # state_orchestrateur peut prendre les valeurs :
        # 0 = pas orchestrateur,
        # 1 = petit orchestrateur (chef de chunk_agents)
        # 2 = gros orchestrateur (chef de lieutenant_agents),
