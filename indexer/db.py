import psycopg2


class IndexerDatabase:
    def __init__(self, db_host, db_user, db_password, db_name, db_port, table_name):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.create_table_if_not_exists(table_name)

    def create_table_if_not_exists(self, table_name):
        cur = self.connection.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS game_specs
        (id serial, name text, original_file_name text, version text, PRIMARY KEY (id))
        """, (table_name,))

    def insert(self, data):
        cur = self.connection_cursor()
        cur.execute("""
        INSERT INTO game_specs() VALUES ()})""", data)
