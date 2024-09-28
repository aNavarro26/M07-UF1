# Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari,
# indicar quants caràcters té i indicar el primer, i l’últim caràcter. (mirar split())
# GUIA pas a pas de mostra:
# Demanar a l’usuari les paraules.
# Utilitzar split().
# Validar el número de paraules insertat
# Imprimir resposta per pantalla """

userInput = input("Introdueix d'una a tres paraules separades per espais: ")

# Divido l'entrada de l'usuari en paraules separades en funció del caràcter d'espai.
paraules = userInput.split(" ")

# Validar el nombre de paraules introduïdes per l'usuari. El
# bucle while comprova si la longitud de la llista paraules és superior a 3 o inferior a 1. Si el
# es compleix, demana a l'usuari que torni a introduir les paraules amb un missatge que indica que a
# es poden introduir com a màxim 3 paraules. Després, la nova entrada es divideix en paraules i la guardo en "paraules".
while len(paraules) > 3 or len(paraules) < 1:
    userInput = input("Com a màxim has de posar 3 paraules, torna a posarles: ")
    paraules = userInput.split(" ")


# Gestiono els diferents casos en funció del nombre de paraules
# d'entrada per l'usuari.
if len(paraules) == 1:
    paraula1 = paraules[0]
    p1Len = len(paraula1)

    print("\n Paraules indicades \n")

    print(
        f"\n {paraula1}: té {p1Len} caràcters. Primer caràcter --> {paraula1[0]}. Últim caràcter --> {paraula1[-1]} \n "
    )

elif len(paraules) == 2:
    paraula1 = paraules[0]
    paraula2 = paraules[1]

    p1Len = len(paraula1)
    p2Len = len(paraula2)

    print("\n Paraules indicades \n")

    print(
        f"\n {paraula1}: té {p1Len} caràcters. Primer caràcter --> {paraula1[0]}. Últim caràcter --> {paraula1[-1]} \n "
    )

    print(
        f"\n {paraula2}: té {p2Len} caràcters. Primer caràcter --> {paraula2[0]}. Últim caràcter --> {paraula2[-1]} \n "
    )

else:
    paraula1 = paraules[0]
    paraula2 = paraules[1]
    paraula3 = paraules[2]

    p1Len = len(paraula1)
    p2Len = len(paraula2)
    p3Len = len(paraula3)

    print("\n Paraules indicades \n")

    print(
        f"{paraula1}: té {p1Len} caràcters. Primer caràcter --> {paraula1[0]}. Últim caràcter --> {paraula1[-1]} \n "
    )

    print(
        f"\n {paraula2}: té {p2Len} caràcters. Primer caràcter --> {paraula2[0]}. Últim caràcter --> {paraula2[-1]} \n "
    )

    print(
        f"\n {paraula3}: té {p3Len} caràcters. Primer caràcter --> {paraula3[0]}. Últim caràcter --> {paraula3[-1]} \n "
    )
