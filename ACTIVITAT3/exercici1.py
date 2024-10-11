# Demanar a l’usuari un número entre 10 i 100. Posar els números a una tupla desde 1 fins al número indicat per l’usuari.
# Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).

userInput = int(input("Introdueix un número entre el 10 i el 100: "))

# Comprovar que el interval es correcte
while userInput < 10 or userInput > 100:
    userInput = int(
        input("Valor no vàlid, introdueix un número entre el 10 i el 100: ")
    )

numTupla = ()

# iterar des de l'1 fins a userInput inclòs. Per a cada numero, es crea una tupla amb aquest i
# després s'afegeix a la tupla

for num in range(1, userInput + 1):
    numTupla = numTupla + (num,)

print(f"Tupla del 1 al {userInput}: {numTupla}")
