# Aquest mòdul proporciona funcions per generar números aleatoris
import random

# Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100.
# Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti
# i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.

secretNumber = random.randint(1, 100)

userInput = int(input("Introdueix un número: "))

tries = 0

isNumCorrect = False

# Continua executant-se mentre la condició "not isNumCorrect" és certa. Continuarà funcionant fins que
# la variable isNumCorrect es converteix en True.
while not isNumCorrect:
    # Bucle de validació que garanteix l'entrada de l'usuari es manté dins del rang d'1 a 100.
    while userInput < 1 or userInput > 100:
        userInput = int(
            input("Introdueix un valor entre el rang seleccionat (1 entre 100): ")
        )

    # Gestiona l'entrada de l'usuari i proporciona comentaris segons en
    # si l'entrada és major, menor o igual al número secret
    if userInput > secretNumber:
        tries += 1
        userInput = int(
            input(f" {userInput} massa gran, indica nou número ({tries} intents): ")
        )
    elif userInput < secretNumber:
        tries += 1
        userInput = int(
            input(f" {userInput} massa petit, indica nou número ({tries} intents): ")
        )
    else:
        isNumCorrect = True
        tries += 1
        print(f"Enhorabona, has encertat. Número d'intents: {tries}")
