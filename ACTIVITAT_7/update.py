import connection as conn


def update_record(
    table_name,
    record_id,
    title=None,
    author=None,
    genre=None,
    pages=None,
    price=None,
    editorial=None,
):
    connection = conn.get_connection()

    if connection:
        try:
            cursor = connection.cursor()

            # començo a fer la consulta, fins que no hi ha ; no s'executa
            query = f"UPDATE {table_name} SET "

            # si el camp te valor ho afegeixo
            if title is not None:
                query += f"title = '{title}', "

            if author is not None:
                query += f"author = '{author}', "

            if genre is not None:
                query += f"genre = '{genre}', "

            if pages is not None:
                query += f"pages = {pages}, "

            if price is not None:
                query += f"price = '{price}', "

            if editorial is not None:
                query += f"editorial = '{editorial}', "

            # elimino la ultima coma
            query = query.rstrip(", ") + f" WHERE id = {record_id};"

            cursor.execute(query)
            connection.commit()

            print("Registre actualitzat.")

        except Exception as e:
            print(f"Error al intentar actualitzar el registre: {e}")
            connection.rollback()  # Faig un rollback perquè hi ha hagut error
        finally:
            cursor.close()
            connection.close()
    else:
        print("No s'ha pogut establir la connexió amb la base de dades.")
