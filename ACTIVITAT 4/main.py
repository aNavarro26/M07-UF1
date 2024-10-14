import exercici1
import exercici2
import exercici3
import exercici4_adrianNavarr


def mostrar_exercici1():
    print("Exercici 1:")

    matriuEx1 = exercici1.exercici1()

    print("Matriu generada: ")
    print(matriuEx1)

    print(f"Dimensió: {matriuEx1.shape}")

    print(f"Tamany: {matriuEx1.size}")

    print(f"Número total d'elements: {matriuEx1.size}")

    print(f"Tipus d'elements interns: {matriuEx1.dtype}")


def mostrar_exercici2():
    print("\nExercici 2: ")

    matriu1Ex2 = exercici2.crear_array1()
    print(f"Array 1: {matriu1Ex2}")
    print(f"Número total d'elements Array1: {matriu1Ex2.size}")
    print(f"Dimensió Array1: {matriu1Ex2.shape}")
    print(f"Tipus d'elements interns Array1: {matriu1Ex2.dtype}")
    print(f"Tamany Array1 en bytes: {matriu1Ex2.nbytes}\n")

    matriu2Ex2 = exercici2.crear_array2()
    print(f"Array 2: {matriu2Ex2}")
    print(f"Número total d'elements Array2: {matriu2Ex2.size}")
    print(f"Dimensió Array2: {matriu2Ex2.shape}")
    print(f"Tipus d'elements interns Array2: {matriu2Ex2.dtype}")
    print(f"Tamany Array2 en bytes: {matriu2Ex2.nbytes}\n")

    matriu3Ex2 = exercici2.crear_array3()
    print(f"Array 3: {matriu3Ex2}")
    print(f"Número total d'elements Array3: {matriu3Ex2.size}")
    print(f"Dimensió Array3: {matriu3Ex2.shape}")
    print(f"Tipus d'elements interns Array3: {matriu3Ex2.dtype}")
    print(f"Tamany Array3 en bytes: {matriu3Ex2.nbytes}\n")


def mostrar_exercici3():
    print("Exercici 3:")

    matriuEx3 = exercici3.generar_matriu()
    print("Matriu original: ")
    exercici3.mostrar_matriu(matriuEx3)

    valor_max, valor_min = exercici3.max_min_matriu(matriuEx3)
    print(f"Valor màxim de la matriu: {valor_max}")
    print(f"Valor mínim de la matriu: {valor_min}")


def mostrar_exercici4():
    print("\nExercici 4: ")

    array1, arrayModificada1, arrayModificada2 = exercici4_adrianNavarr.exercici4()

    print("Matriu 1 generada de 3x4: ")
    print(array1)

    print("\nMatriu 2 de 4x3 amb les files i columnes intercanviades: ")
    print(arrayModificada1)

    print(
        "\nMatriu 3 amb la última columna canviada per el últim valor de la primera fila: "
    )
    print(arrayModificada2)


def main():
    mostrar_exercici1()
    mostrar_exercici2()
    mostrar_exercici3()
    mostrar_exercici4()


if __name__ == "__main__":
    main()
