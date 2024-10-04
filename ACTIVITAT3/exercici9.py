# Llistat de notes. Crear una lista amb 6 assignatures (poden ser mòduls de cicles o assignatures de secundaria).
# Demana a l’usuari que indiqui les notes de cada assignatura i emmagatzema-les en una altra llista. Mostrar per
# pantalla el missatge A <assignatura> ha tret <nota>. Intenta millorar aquest programa utilitzant altres tipus de dades explicats.
# Cal que l’exercici tingui les dues versions.


def exercici9():
    # Demanar a l'usuari que seleccioni la versió del programa
    userInput = input("Selecciona la versió (1 o 2): ")

    if userInput == "1":
        # Versió 1
        assignatures = [
            "Serveis en Xarxa",
            "Cloud",
            "Seguretat Informàtica",
            "Bases de Dades",
            "Aplicacions Web",
            "Disseny d'Interfícies Web",
        ]

        notesFinals = []  # Inicialitzar la llista

        for assignatura in assignatures:
            # Demanar la nota per a cada assignatura
            nota = input(f"Introdueix la nota per a {assignatura}: ")
            notesFinals.append(nota)  # Afegir la nota a la llista

        for i in range(len(assignatures)):
            # Mostrar el missatge amb la nota per a cada assignatura
            print(f"A {assignatures[i]} ha tret {notesFinals[i]}.")

    elif userInput == "2":
        # Versió 2, diccionari amb Key Assignatura i Value la Nota de la signatura
        assignatures = [
            "Serveis en Xarxa",
            "Cloud",
            "Seguretat Informàtica",
            "Bases de Dades",
            "Aplicacions Web",
            "Disseny d'Interfícies Web",
        ]

        notesFinals = {}  # Inicialitzar el diccionari

        for assignatura in assignatures:
            # Demanar la nota per a cada assignatura
            nota = input(f"Introdueix la nota per a {assignatura}: ")
            notesFinals[assignatura] = nota  # Afegir la nota al diccionari

        for assignatura, nota in notesFinals.items():
            # Mostrar el missatge amb la nota per a cada assignatura
            print(f"A {assignatura} ha tret {nota}.")
    else:
        # Gestionar el cas d'entrada no vàlida
        print("Valor no vàlid")
        exercici9()  # Tornar a demanar l'entrada de l'usuari


exercici9()
