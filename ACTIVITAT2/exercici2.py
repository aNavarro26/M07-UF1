# Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i
# finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final
# amb l’IVA afegit. Si no afegeix el IVA correcte, tornar a demanar el IVA fins que posi un dels 3 vàlids.

userInputValue = float(input("Introdueix un valor en €: "))


# Assegurar que l'usuari introdueix un valor vàlid superior a 0
# per l'import inicial en euros.
while userInputValue <= 0:
    print("Introdueix un valor vàlid")
    userInputValue = float(input("Introdueix un valor en €: "))

userInputIVA = int(input("Introdueix l'IVA a aplicar (4%, 10%, 21%): "))

# Garanteixo que l'usuari introdueixi un valor vàlid per a l'IVA
# que s'ha d'aplicar, que hauria de ser del 4%, del 10% o del 21%.
while userInputIVA != 4 and userInputIVA != 10 and userInputIVA != 21:
    print("Introdueix un IVA dels 3 vàlids (4%, 10%, 21%)")
    userInputIVA = int(input("Introdueix l'IVA a aplicar (4%, 10%, 21%): "))

# Calcula l'import final després d'aplicar l'IVA corresponent
# basada en l'entrada de l'usuari.
if userInputIVA == 4:
    amount = userInputValue * 1.04
elif userInputIVA == 10:
    amount = userInputValue * 1.10
elif userInputIVA == 21:
    amount = userInputValue * 1.21

print(
    f"Valor indicat: {userInputValue:.2f} \nImport d'IVA demanat: {userInputIVA} \nResultat final amb IVA afegit: {amount:.2f}"
)
