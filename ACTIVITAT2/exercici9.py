# Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla les dues paraules amb els dos
# primers caràcters de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.

userInput = input("Introdueix dos paraules separades per espais: ")

paraules = userInput.split(" ")

while len(paraules) != 2:
    userInput = input("Com a mínim i com a màxim has de posar 2 paraules: ")
    paraules = userInput.split(" ")

paraula1Orig = paraules[0]
paraula2Orig = paraules[1]

chars1Pack = paraula1Orig[0:2]
chars2Pack = paraula2Orig[0:2]

paraula1Mod = chars2Pack + paraula1Orig[2:]
paraula2Mod = chars1Pack + paraula2Orig[2:]

print(
    f"Paraules originals: {paraula1Orig} {paraula2Orig} \nParaules modificades: {paraula1Mod} {paraula2Mod}"
)
