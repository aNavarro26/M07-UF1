# Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari,
# indicar quants caràcters té i indicar el primer, i l’últim caràcter. (mirar split())
# GUIA pas a pas de mostra:
# Demanar a l’usuari les paraules.
# Utilitzar split().
# Validar el número de paraules insertat
# Imprimir resposta per pantalla """

userInput = input("Introdueix d'una a tres paraules separades per espais: ")

paraules = userInput.split(" ")

while len(paraules) > 3 or len(paraules) < 1:
    userInput = input("Com a màxim has de posar 3 paraules, torna a posarles: ")
    paraules = userInput.split(" ")


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
