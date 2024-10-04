# Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a
# l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari).
# Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

contactes = {}
continuar = True

while continuar:
    userInput = input("Introdueix un nom (o 'no' per acabar): ")
    # Si l'usuari vol acabar
    if userInput.lower() == "no":
        continuar = False
    # Si el nom ja existeix en el diccionari
    elif userInput in contactes:
        print(f"El nom '{userInput}' ja existeix.")
        userInput = input("Introdueix un altre nom (o 'no' per acabar): ")
        # Comprovar de nou si vol acabar
        if userInput.lower() == "no":
            continuar = False
    else:
        # Demanar l'edat per al nou contacte
        edatInput = input(f"Introdueix l'edat de {userInput}: ")

        # Comprovar que l'edat sigui un número
        while not edatInput.isdigit():
            print("Error: Introdueix una edat vàlida (només números).")
            edatInput = input(f"Introdueix l'edat de {userInput}: ")

        # Afegir el nou contacte al diccionari
        contactes[userInput] = edatInput
        print(f"Contacte afegit: {userInput}, amb {edatInput} anys.")

print("\nContactes introduïts:")
for nom, edat in contactes.items():
    print(f"{nom}: {edat} anys")
