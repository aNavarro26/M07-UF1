import numpy as np

def modificar_matriu():
    # Crear una matriu de 3x4 amb números aleatoris de 0 a 80
    matriu = np.random.randint(0, 81, size=(3, 4))
    print("Matriu original 3x4:")
    print(matriu)
    
    # Extraure l'última fila de la matriu original
    ultima_fila = matriu[-1, :]
    
    # Crear una nova matriu de 4x3 inicialitzada amb zeros
    matriu_modificada = np.zeros((4, 3), dtype=int)
    
    # Copiar les primeres dues files de la matriu original a les primeres dues files de la matriu modificada
    matriu_modificada[0:2, :] = matriu[0:2, 0:3]
    
    # Copiar l'última fila de la matriu original a l'última columna de la matriu modificada
    matriu_modificada[:, 2] = ultima_fila
    
    print("Matriu modificada a 4x3, l'última fila a l'última columna:")
    print(matriu_modificada)
    
    # Fer que tots els elements de l'última columna siguin iguals al primer element d'aquesta columna
    primer_valor_ultima_columna = matriu_modificada[0, 2]
    matriu_modificada[:, 2] = primer_valor_ultima_columna
    
    print("Matriu final amb l'última columna igualada:")
    print(matriu_modificada)



modificar_matriu()