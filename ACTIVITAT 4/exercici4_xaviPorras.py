import numpy as np

def exercici4():
    # Creo una matriz de 3x4 con números aleatorios entre 0 y 80
    matriuOriginal = np.random.randint(0, 80, size=(3, 4))
    
    print(f"Matriz original (3x4):\n{matriuOriginal}\n")
    
    # Creo una nueva matriz vacía de 4x3
    matriuModificada = np.zeros((4, 3), dtype=int)
    
    for i in range(3):  # Recorro las 3 primeras columnas de la matriz original
        matriuModificada[0:3, i] = matriuOriginal[0:3, i]   #Le asigno los valores a la array modificada
    
    for i in range(4):  # Recorremos las 4 columnas de la matriz original
        matriuModificada[i, 2] = matriuOriginal[2, i]
    
    # Asigno los dos primeros valores de la ultima fila de la array modificada
    matriuModificada[3, 0] = matriuOriginal[0, 3] 
    matriuModificada[3, 1] = matriuOriginal[1, 3]
    
    print(f"Matriz modificada:\n {matriuModificada}\n")
    
    valor_primero = matriuModificada[0, 2]  # Primer valor de la última columna
    matriuModificada[:, 2] = valor_primero  # Asigno este valor a toda la última columna

    print(f"Matriz final:\n {matriuModificada}")

exercici4()
