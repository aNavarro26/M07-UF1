import psycopg2


def get_connection():

    try:
        connection = psycopg2.connect(
            database="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="localhost",
            port="5432",
        )
        cursor = connection.cursor()
        return connection

        print(cursor)
    except Exception as e:
        print(f"Error al establir la connexió amb la base de dades {e}")
    finally:
        cursor.close()
        connection.close()
        return None
