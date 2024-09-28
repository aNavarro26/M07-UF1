# Demanar a l’usuari que introdueixi un número. Mostrar per pantalla la suma de tots els números començant
# amb l’1 fins el número indicat per l’usuari.

userInput = int(input("Introdueix un número: "))

sum = 0

# Comprova si l'entrada de l'usuari és inferior a 1. Llavors no es vàlida i torna a preguntar
while userInput < 1:
    userInput = int(input("Valor no vàlid, introdueix un número: "))


# Itera sobre un interval de números que comença des de l'1 fins al
# número introduït per l'usuari (userInput) i els va sumant a la variable sum.
for i in range(1, userInput + 1):
    sum += i

print(f"Suma total entre 1 fins a {userInput}: {sum}")
