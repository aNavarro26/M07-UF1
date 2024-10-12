import numpy as np

def generar_matriu():
    # Demanar a l'usuari les dimensions de la matriu
    filas = int(input("Introdueix el nombre de files: "))
    columnas = int(input("introdueix el nombre de columnes: "))
    
    # Genera una matriu amb numeros aleatoris entre 0 i 100
    matriu = np.random.randint(0, 101, size=filas * columnas)
    matriu = matriu.reshape(filas, columnas)
    return matriu

def mostrar_matriu(matriu):
    print(matriu)

def max_min_matriu(matriu):
    # Troba el valor màxim i mínim de la matriu
    valor_max = matriu.max()
    valor_min = matriu.min()
    return valor_max, valor_min

def main():
    # Genera i mostra la matriu original
    matriu = generar_matriu()
    mostrar_matriu(matriu, "Matriu Original")
    
    # Demana a l'usuari noves dimensions per a redimensionar la matriu
    nuevas_filas = int(input("Introdueix les noves files per a redimensionar la matriu: "))
    nuevas_columnas = int(input("Introdueix les noves columnes per a redimensionar la matriu: "))
    
    # Assegura que el total d'elements sigui el mateix per a redimensionar
    if nuevas_filas * nuevas_columnas != matriu.size:
        print("Error: El nombre total d'elements ha de ser el mateix.")
        return
    
    # Redimensiona i mostra la matriu
    matriu = matriu.reshape(nuevas_filas, nuevas_columnas)
    mostrar_matriu(matriu, "Matriu Redimensionada")
    
    # Troba i mostra els valors màxim i mínim
    maximo, minimo = max_min_matriu(matriu)
    print(f"El valor màxim de la matriu és: {maximo}")
    print(f"El valor mínim de la matriu és: {minimo}")

if __name__ == "__main__":
    main()