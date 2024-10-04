# Emmagatzema l’abecedari en una llista. Elimina de la llista les lletres que ocupin les posicions múltiples de 3.
# Converteix la llista resultant en una tupla i mostra la llista i la tupla per pantalla.

abcList = list("abcdefghijklmnopqrstuvwxyz")  # Guardar l'abecedari en una llista

abcModified = []  # Inicialitzar una llista buida per a les lletres modificades

# Recorrer cada lletra de l'abecedari amb el seu índex
for i, letra in enumerate(abcList):
    # Comprovar si la posició (índex + 1) no és múltiple de 3
    if (i + 1) % 3 != 0:
        abcModified.append(letra)  # Afegir la lletra a la llista modificada

abcModifiedTupla = tuple(abcModified)  # Convertir la llista en una tupla

# Mostrar l'abecedari original
print(f"Abecedari normal: {abcList}")

# Mostrar la llista resultant sense les lletres en posicions múltiples de 3
print(f"Llista resultant: {abcModified}")

# Mostrar la tupla resultant amb les lletres modificades
print(f"Tupla resultant: {abcModifiedTupla}")
