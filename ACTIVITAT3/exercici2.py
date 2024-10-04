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
    # comprovar si l'entrada de l'usuari és un número de mes vàlid.
    while userInput < 0 or userInput > 12:
        userInput = int(
            input(
                "Mes no vàlid, introdueix un mes en format número (1 al 12, per finalitzar posa 0): "
            )
        )

    # accedo a l'element del mesosTupla corresponent a l'entrada de l'usuari. L'entrada de l'usuari ha de ser un número entre 1 i
    # 12, per això resto 1 de l'entrada de l'usuari per obtenir l'índex correcte a la tupla

    mesEscollit = mesosTupla[userInput - 1]
    print(f"El número {userInput} correspon al mes: {mesEscollit}")
    userInput = int(
        input("Introdueix un mes en format número (1 al 12, per finalitzar posa 0): ")
    )
