# Crear un diccionari de divises amb els seus símbols (exemple: Euro:€…). Demana a l’usuari una divisa
# i mostra el seu símbol. Si la divisa no està al diccionari mostra un missatge.


# Diccionari divises colaboracion con ChatGPT
divises = {
    "Euro": "€",
    "Dòlar dels Estats Units": "$",
    "Lliura esterlina": "£",
    "Ien japonès": "¥",
    "Franc suís": "CHF",
    "Dòlar canadenc": "CAD",
    "Dòlar australià": "AUD",
    "Yuan xinès": "¥",
    "Peso mexicà": "MXN",
    "Rupia índia": "₹",
    "Real brasiler": "R$",
    "Rublo rus": "₽",
    "Peso argentí": "$",
    "Won sud-coreà": "₩",
    "Corona noruega": "NOK",
    "Corona sueca": "SEK",
    "Corona danesa": "DKK",
    "Lira turca": "₺",
    "Ringgit de Malàisia": "RM",
    "Rand sud-africà": "R",
    "Baht tailandès": "฿",
}

# Mostrar les divises disponibles al diccionari
print("Divises disponibles:", ", ".join(divises.keys()))
# Demanar a l'usuari que introdueixi una divisa
userInput = input("Introdueix una divisa: ")

# Comprovar si la divisa introduïda no està al diccionari
while userInput not in divises:
    # Si no està, demanar una nova divisa
    userInput = input(
        f"La divisa {userInput} no està al diccionari, introdueix un altre: "
    )

# Mostrar el símbol de la divisa si es troba al diccionari
print(f"Símbol de la divisa {userInput}: {divises[userInput]}")
