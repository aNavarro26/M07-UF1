# LOOPS: Mostrar els números imparells de l’1 al 500 amb for.

print("\nNums imparells de l'1 al 500: \n")

num = 1

# Bucle "for" per iterar sobre números de l'1 al 500.
# Per a cada nombre d'aquest rang, comprova si el nombre és senar utilitzant la condició. Si el nombre és senar
# (la resta de dividir el nombre per 2 no és igual a 0), # imprimeix el número amb `print(num)`.
for num in range(1, 501):
    if num % 2 != 0:
        print(num)
