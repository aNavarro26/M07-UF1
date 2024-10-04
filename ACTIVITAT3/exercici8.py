# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista.
# Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:


userInput = input("Introdueix 10 números separats per espais: ")
numsArrayString = list(userInput.split())

numsArray = []

# Convertir cada número de la cadena a float i afegir-los a numsArray
for number in numsArrayString:
    numsArray.append(float(number))

# Comprovar que la longitud de numsArray sigui 10
while len(numsArray) != 10:
    # Si no té exactament 10 números demanar a l'usuari que introdueixi 10 números vàlids
    userInput = input(
        "Valors no vàlids, introdueix exactament 10 números separats per espais: "
    )

    # Separar els números introduïts per l'usuari i guardarlos en una llista
    numsArrayString = list(userInput.split())

    # Reiniciar numsArray
    numsArray = []

    # Convertir els números a float i afegir-los a numsArray
    for number in numsArrayString:
        numsArray.append(float(number))


print(f"Números de l'usuari: {numsArray}")
print(f"Suma total: {sum(numsArray)}")
print(f"Mitjana: {sum(numsArray) / len(numsArray)}")
