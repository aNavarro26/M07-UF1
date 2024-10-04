# Cal buscar la informació que es demana de la següent list:

areas_pis = [
    "Menjador",
    10.15,
    "Rebedor",
    9.56,
    "Habitació1",
    12.34,
    "Terrassa",
    15.55,
    "Lavabo",
    7.98,
    "Cuina",
    12,
    "Habitació2",
    12.23,
]

# Imprimir el segon element

print(areas_pis[1:2])

# Imprimir l’últim element

print(areas_pis[-1:])

# Imprimir l’àrea de la terrassa

indexTerrassa = areas_pis.index("Terrassa")
print(areas_pis[indexTerrassa + 1 : indexTerrassa + 2])

# Imprimir del primer element al tercer element

print(areas_pis[0:3])

# Imprimir del tercer element a l’últim

print(areas_pis[2:])

# Imprimir el total de l'àrea de les dues habitacions

indexHab1 = areas_pis.index("Habitació1")
indexHab2 = areas_pis.index("Habitació2")

print(areas_pis[indexHab1 + 1] + areas_pis[indexHab2 + 1])

# Modificar l’àrea del lavabo i imprimir la nova list area

indexLab = areas_pis.index("Lavabo")
areas_pis[indexLab + 1] = 33.33

print(areas_pis[indexLab + 1 : indexLab + 2])

# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.

areas_pis.append("Pati interior")
areas_pis.append(2.78)
print(areas_pis)

# Imprimir el total de l’àrea del pis.

suma = 0

for value in areas_pis:
    if type(value) == float:
        suma += value

print(suma)
