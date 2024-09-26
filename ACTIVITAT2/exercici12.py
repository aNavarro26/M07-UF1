# Demanar a l’usuari que introdueixi un número. Mostrar per pantalla la suma de tots els números començant
# amb l’1 fins el número indicat per l’usuari.

userInput = int(input("Introdueix un número: "))

sum = 0

while userInput < 1:
    userInput = int(input("Valor no vàlid, introdueix un número: "))


for i in range(1, userInput + 1):
    sum += i

print(f"Suma total entre 1 fins a {userInput}: {sum}")
