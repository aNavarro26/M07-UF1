# Demanar a l’usuari dos valors. Una vegada s’executa el programa, aquest ha de mostrar el resultat
# (suma, resta, divisió o multiplicació)  per pantalla.

userValue1 = float(input("Introdueix el valor 1: "))
userValue2 = float(input("Introdueix el valor 2: "))

# Comprova si el valor de "userValue1" és inferior a
# 0. Si la condició és certa ("userValue1" és inferior a 0), demano a l'usuari que introdueixi un
# valor vàlid mostrant el missatge i després demano a l'usuari que introdueixi el
# valor nou per a userValue1. Continuarà en bucle fins que l'usuari introdueix un valor que no sigui inferior a 0.
while userValue1 < 0:
    print("Introdueix un valor valid")
    userValue1 = float(input("Introdueix el valor 1: "))

while userValue2 < 0:
    print("Introdueix un valor valid")
    userValue2 = float(input("Introdueix el valor 2: "))

# Demano a l'usuari que introdueixi l'operació que vol dur a terme
userOperator = input(
    "Introdueix l'operació a fer (suma, resta, divisio, multiplicacio): "
).lower()

# Valido l'entrada de l'usuari per a l'operació que vol fer
# realitzar (ja sigui suma, resta, divisió o multiplicació).
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

# Realitzo l'operació basada en l'entrada de l'usuari
# per a l'operador.
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
