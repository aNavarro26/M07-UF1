import connection as conn


def create_table(table_name):
    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(20),
                    author VARCHAR(20),
                    gender VARCHAR(20),
                    pages INTEGER,
                    price VARCHAR(20),
                    editorial VARCHAR(20)
                    );
            """

            cursor.execute(query)

        except Exception as e:
            raise e

        finally:
            cursor.close()
            connection.close()
