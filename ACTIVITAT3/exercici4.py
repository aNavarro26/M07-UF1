# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà
# en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

userInput = input("Introdueix 10 números separats per espais: ")

numsTupla = ()

# iterar sobre l'entrada que és una cadena que conté
# nombres separats per e espais.

for num in userInput.split():
    numsTupla = numsTupla + (int(num),)

lenTupla = len(numsTupla)

# Comprovar si l'usuari ha introduït exactament 10 números separats per espais.
# Si la longitud de la tupla numsTupla no és igual a 10, tornar a demanar a l'usuari
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
