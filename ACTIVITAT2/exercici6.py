# LOOPS: Mostrar els números de l’1 al 100 amb un while. Fer el mateix exercici amb for.

print("\nExercici amb While: \n")

num = 1

# Bucle "while" per imprimir números de l'1 al 100.
while num <= 100:
    print(num)
    num += 1

print("\nExercici amb un for: \n")

num = 1

# Bucle "for" per iterar en un interval de números de l'1 al 100.
for num in range(1, 101):
    print(num)
