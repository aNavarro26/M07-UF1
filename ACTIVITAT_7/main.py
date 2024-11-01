import connection, create, create_table, read, update, delete

""" create_table.create_book_table("libro")

create.create_record(
    "libro",
    "Return",
    "Alan Wake",
    "Suspense Psicológico",
    "320",
    665,
    "Editorial Cauldron Lake",
)

read.read_record("libro")

update.update_record("libro", "")

delete.delete_record()


create.create_record("tableTest1", "adrian", "navarro", 19) """


def mostrar_menu():
    print("\n============ CRUD ============")
    print("1. Crear un registre")
    print("2. Llegir tots els registres")
    print("3. Actualitzar un registre")
    print("4. Eliminar un registre")
    print("5. Sortir")
    print("===============================\n")


def main():
    create_table.create_book_table("libro")  # Creo la tabla al iniciar-ho

    while True:
        mostrar_menu()

        user_input = input("Selecciona l'opció (1-5): ")

        if user_input == "1":
            # guardo en varibles les dades que introduirà
            title = input("Introdueix el títol: ")
            author = input("Introdueix l'autor: ")
            genre = input("Introdueix el gènere: ")
            pages = int(input("Introdueix el número de pàgines: "))
            price = float(input("Introdueix el preu: "))
            editorial = input("Introdueix l'editorial: ")

            create.create_record("libro", title, author, genre, pages, price, editorial)

        elif user_input == "2":
            read.read_record("libro")

        elif user_input == "3":
            # Actualizar un registro
            record_id = input("Introdueix l'ID del registre que vols actualitzar: ")
            print("Introdueix els nous valors (deixa en blanc per no modificar):")

            title = input("Nou títol: ")
            author = input("Nou autor: ")
            genre = input("Nou gènere: ")
            pages = input("Noves pàgines: ")
            price = input("Nou preu: ")
            editorial = input("Nova editorial: ")

            update.update_record(
                "libro",
                record_id,
                # si title té valor s'ho pasa, si no ho deixa en None
                title if title else None,
                author if author else None,
                genre if genre else None,
                pages if pages else None,
                price if price else None,
                editorial if editorial else None,
            )

        elif user_input == "4":
            delete.delete_record("libro")

        elif user_input == "5":
            print("Sortint del programa...")
            break
        else:
            print("Opció no vàlida. Escolliu una opció del menú (1-5).")


if __name__ == "__main__":
    main()
