# Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.

userValue = int(input("Introdueix un número: "))

while userValue < 0:
    userValue = int(input("Introdueix un valor vàlid: "))

if userValue % 2 == 0:
    print(f"El número {userValue} és parell")
else:
    print(f"El número {userValue} és senar")
