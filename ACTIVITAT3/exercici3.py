# Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10.
# Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30

userInput = int(input("Introdueix un número de l'1 al 10: "))

while userInput < 1 or userInput > 10:
    userInput = int(input("Número no vàlid, introdueix un número de l'1 al 10: "))

resultsArray = []

num = 0

for num in range(1, 11):
    result = userInput * num
    resultsArray.append(result)


resultsArray = [str(result) for result in resultsArray]

# Amb el resultsArray[:-2] agafo tots els elements menys els 2 últims que hi ha. En resultsArray[-2] agafo
# només el penúltim element i després agafo l'últim element amb -1, i és un f-string per a que pugui afegir la "i"
# en mig dels dos últims.

print(", ".join(resultsArray[:-2] + [f"{resultsArray[-2]} i {resultsArray[-1]}"]))
