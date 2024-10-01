# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà
# en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

userInput = input("Introdueix 10 números separats per espais: ")

numsTupla = ()

for num in userInput.split():
    numsTupla = numsTupla + (int(num),)

lenTupla = len(numsTupla)

while lenTupla != 10:
    userInput = input(
        "Números no vàlids, introdueix exactament 10 números separats per espais: "
    )
    numsTupla = ()
    for num in userInput.split():
        numsTupla = numsTupla + (int(num),)

    lenTupla = len(numsTupla)


print(
    f"Tupla de menor a major: {sorted(numsTupla)}"
)  # numsTupla, reverse=True para que sea de major a menor
