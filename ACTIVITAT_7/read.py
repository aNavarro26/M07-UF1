import connection as conn


def read_record(table_name):
    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            query = f"""
                SELECT * FROM {table_name};
                """

            cursor.execute(query)

            records = cursor.fetchall()

            for rec in records:
                print(rec)

        except Exception as e:
            raise e
        finally:
            cursor.close()
            connection.close()
