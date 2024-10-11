# Demanar a l’usuari que introdueixi un número. Mostrar per terminal la taula de multiplicar del número indicat per l’usuari.

userInput = int(input("Introdueix un número: "))

num = 0

# Iterar sobre els números del 0 al 10 (inclosos) mitjançant
# la funció rang(0, 11).
for num in range(0, 11):
    # Mostro la taula de multiplicar del nombre introduït per l'usuari. Printo l'operació
    # "número x multiplicador = resultat"
    # on:
    # - {userInput} és el número introduït per l'usuari.
    # - {num} és el multiplicador actual que s'utilitza en el bucle.
    # - {userInput * num} calcula el resultat de multiplicar el nombre introduït per l'usuari amb el
    # multiplicador actual.
    print(f" {userInput} x {num} = {userInput * num}")
