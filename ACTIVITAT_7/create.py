import connection as conn


def create_record(table_name, title, author, genre, pages, price, editorial):
    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            query = f"""
                INSERT INTO {table_name} (title, author, genre, pages, price, editorial) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            # cursor.execute(query)

            # se lo paso con una tupla para evitar SQLInjection
            cursor.execute(query, (title, author, genre, pages, price, editorial))

            connection.commit()

        except Exception as e:
            # connection.rollback()
            raise e

        finally:
            cursor.close()
            connection.close()
