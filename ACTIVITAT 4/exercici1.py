import numpy as np

# (A)Trucar a l’exercici 1 i mostrar per pantalla:
# La matriu com la de la imatge de l’exercici 1
# La dimensió de la matriu
# El tamany de la matriu
# Número total d’elements
# Tipus d’elements interns
# 	Cada punt ha de vindre acompanyat d’un text on quedi clar què s’està mostrant per pantalla.

# Crearà un ndarray com la de la imatge. La matriu que es mostra és una matriu on només es vol números ascendents
# en la diagonal de 0 a 49.  (mirar el següent enllaç)
# Guardar la ndarray en un arxiu de nom exercici1.npy.


def exercici1():
    # creo una matriu NumPy de 50x50 plena de zeros especificant el tipus de dades dels elements de la matriu com a int.
    array = np.zeros((50, 50), dtype=int)

    # Omplo la diagonal de la matriu amb valors de 0 a 49. np.arange(50) crea una matriu de nombres de 0 a 49.
    # i la funció "np.fill_diagonal()" omple la diagonal de la matriu d'entrada "array" amb els valors.

    np.fill_diagonal(array, np.arange(50))

    print(array)


exercici1()
