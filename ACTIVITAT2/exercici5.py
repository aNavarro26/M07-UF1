# Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.

userValue = int(input("Introdueix un número: "))

# És un bucle de validació. Comprova si l'entrada de l'usuari és inferior a 0
while userValue < 0:
    userValue = int(input("Introdueix un valor vàlid: "))

# Comprova si el número introduït per l'usuari "userValue" és parell o senar.
if userValue % 2 == 0:
    print(f"El número {userValue} és parell")
else:
    print(f"El número {userValue} és senar")
