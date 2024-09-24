# LOOPS: Mostrar els números imparells de l’1 al 500 amb for.

print("\nNums imparells de l'1 al 500: \n")

num = 1

for num in range(1, 501):
    if num % 2 != 0:
        print(num)
