# Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla
# el mes corresponent al número indicat per l’usuari. El programa finalitza només quan l’usuari posa 0.

mesosTupla = (
    "Gener",
    "Febrer",
    "Març",
    "Abril",
    "Maig",
    "Juny",
    "Juliol",
    "Agost",
    "Setembre",
    "Octubre",
    "Novembre",
    "Desembre",
)

userInput = int(
    input("Introdueix un mes en format número (1 al 12, per finalitzar posa 0): ")
)

while userInput != 0:
    while userInput < 0 or userInput > 12:
        userInput = int(
            input(
                "Mes no vàlid, introdueix un mes en format número (1 al 12, per finalitzar posa 0): "
            )
        )
    mesEscollit = mesosTupla[userInput - 1]
    print(f"El número {userInput} correspon al mes: {mesEscollit}")
    userInput = int(
        input("Introdueix un mes en format número (1 al 12, per finalitzar posa 0): ")
    )
