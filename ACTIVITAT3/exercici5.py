# Demanar a l’usuari una frase. El programa eliminarà els espais i s'afegirà a una tupla. Mostrar per pantalla el contingut de la tupla.
# I mostrar també la frase sense caràcters repetits. Exemple: Usuari indica la paraula caracteristica dels animals. Es mostra per pantalla carteis d nml.

userInput = input("Introdueix una frase: ")

fraseTupla = tuple(userInput.split())

fraseNoDups = []
charDups = []

for word in fraseTupla:
    newWord = ""
    for char in word:
        if char not in charDups:
            charDups.append(char)
            newWord += char
    fraseNoDups.append(newWord)

fraseFinalNoDups = ""
for word in fraseNoDups:
    fraseFinalNoDups += word + " "

fraseFinalNoDups = fraseFinalNoDups.strip()

print(f"Frase sense caràcters repetits: {fraseFinalNoDups}")
