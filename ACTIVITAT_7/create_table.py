import connection as conn


def create_book_table(table_name):
    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(50),
                    author VARCHAR(50),
                    genre VARCHAR(50),
                    pages INTEGER,
                    price FLOAT,
                    editorial VARCHAR(50)
                    );
            """

            cursor.execute(query)
            # faig commit per a que es guardin els canvis
            connection.commit()

        except Exception as e:
            raise e

        finally:
            cursor.close()
            connection.close()
