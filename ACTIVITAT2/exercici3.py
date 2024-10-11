# Demanar a l’usuari que introdueixi 2 valors i mostrar, per pantalla, quin és el més gran. (Utilitzar operador correcte)

userInputValue1 = float(input("Introdueix el valor 1: "))
userInputValue2 = float(input("Introdueix el valor 2: "))

# Compara dos valors d'entrada proporcionats per l'usuari i determina quin és més gran.
if userInputValue1 > userInputValue2:
    print(f"El valor més gran és: {userInputValue1:.2f}")
elif userInputValue2 > userInputValue1:
    print(f"El valor més gran és: {userInputValue2:.2f}")
else:
    print(
        f"El valor 1 <{userInputValue1:.2f}> i el valor 2 <{userInputValue2:.2f}> són iguals"
    )
