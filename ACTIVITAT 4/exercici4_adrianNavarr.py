import numpy as np

# Exercici 4


def exercici4():
    # creo una matriu "array1" 3x4 amb random.randint entre 0 i 80
    array1 = np.random.randint(0, 80, size=(3, 4))

    # print(f"{array1}\n")

    # creu una matriu de 4x3 amb els valors inicialitzats a zero i que siguin de tipo int
    arrayModificada1 = np.zeros((4, 3), dtype=int)

    # recorro les files de la matriu 1
    for i in range(3):
        # recorro les columnes de la matriu 1
        for j in range(3):
            # assigno la fila i i la columna j de la primera a la nova array canviant de posicio per a que sigui la fila la columan
            arrayModificada1[j, i] = array1[i, j]

    # agafo ultima fila agafant tots els elements amb :
    ultimaFila = array1[-1, :]

    # selecciono tota la ultima columna i poso els valors que tinc a ultimaFila
    arrayModificada1[:, -1] = ultimaFila

    # print(arrayModificada1)

    # agafo el primer numero de la última fila
    ultimaColumnaValor = ultimaFila[0]

    # faig una copia de l'array per despres poder retornarla correctament
    arrayModificada2 = np.copy(arrayModificada1)

    # afegeixo la última columna de la nova matriu amb el primer valor
    arrayModificada2[:, -1] = ultimaColumnaValor

    # print(f"\n{arrayModificada1}")

    return array1, arrayModificada1, arrayModificada2


exercici4()
