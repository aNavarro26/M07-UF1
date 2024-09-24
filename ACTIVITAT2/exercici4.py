# Demanar a l’usuari dos valors. Una vegada s’executa el programa, aquest ha de mostrar el resultat
# (suma, resta, divisió o multiplicació)  per pantalla.

userValue1 = float(input("Introdueix el valor 1: "))
userValue2 = float(input("Introdueix el valor 2: "))

while userValue1 < 0:
    print("Introdueix un valor valid")
    userValue1 = float(input("Introdueix el valor 1: "))

while userValue2 < 0:
    print("Introdueix un valor valid")
    userValue2 = float(input("Introdueix el valor 2: "))

userOperator = input(
    "Introdueix l'operació a fer (suma, resta, divisio, multiplicacio): "
).lower()

while (
    userOperator != "suma"
    and userOperator != "resta"
    and userOperator != "divisio"
    and userOperator != "multiplicacio"
):
    print(f"Operador '{userOperator}' no vàlid")
    userOperator = input(
        "Introdueix l'operació a fer (suma, resta, divisio, multiplicacio): "
    ).lower()

if userOperator == "suma":
    result = userValue1 + userValue2
    print(f"Resultat: {userValue1} + {userValue2} = {result:.2f}")
elif userOperator == "resta":
    result = userValue1 - userValue2
    print(f"Resultat: {userValue1} - {userValue2} = {result:.2f}")
elif userOperator == "divisio":
    if userValue2 == 0:
        print(f"No es pot dividir {userValue1} entre {userValue2}")
    else:
        result = userValue1 / userValue2
        print(f"Resultat: {userValue1} / {userValue2} = {result:.2f}")
elif userOperator == "multiplicacio":
    result = userValue1 * userValue2
    print(f"Resultat: {userValue1} * {userValue2} = {result:.2f}")
