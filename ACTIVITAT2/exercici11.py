# Demanar a l’usuari que introdueixi un número. Mostrar per terminal la taula de multiplicar del número indicat per l’usuari.

userInput = int(input("Introdueix un número: "))

num = 0

for num in range(0, 11):
    print(f" {userInput} x {num} = {userInput * num}")
