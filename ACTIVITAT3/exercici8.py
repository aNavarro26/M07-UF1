# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista.
# Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.
# TODO: Comentar Codigo y hacer ej 7

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:


userInput = input("Introdueix 10 números separats per espais: ")
numsArrayString = list(userInput.split())

numsArray = []

for number in numsArrayString:
    numsArray.append(float(number))

while len(numsArray) != 10:
    userInput = input(
        "Valors no vàlids, introdueix exactament 10 números separats per espais: "
    )
    numsArrayString = list(userInput.split())
    numsArray = []
    for number in numsArrayString:
        numsArray.append(float(number))


print(f"Números de l'usuari: {numsArray}")
print(f"Suma total: {sum(numsArray)}")
print(f"Mitjana: {sum(numsArray) / len(numsArray)}")
