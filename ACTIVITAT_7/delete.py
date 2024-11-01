import connection as conn


def delete_record(table_name):
    record_id = input("Introdueix el ID del registre que vols eliminar:  ")

    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            query = f"DELETE FROM {table_name} WHERE id = {record_id};"

            cursor.execute(query)
            connection.commit()

            print(f"Registre amb ID {record_id} eliminat correctament.")

        except Exception as e:
            print(f"No s'ha pogut eliminar el registre: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
    else:
        print("No s'ha pogut establir la connexió amb la base de dades")
