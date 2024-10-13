import numpy as np

def crear_array1():
    array = np.array([88, 23, 39, 41])
    return array

my_array = crear_array1()
print("Array 1:", my_array)
print("Número total de elementos:", my_array.size) # Imprime el número total de elementos
print("Dimensión de la matriz:", my_array.shape) #Imprime las dimensiones de la array
print("Tipo de elementos internos:", my_array.dtype) #Imprime el tipo de datos que contiene la array
print("Tamaño de la matriz en bytes:", my_array.nbytes) #Imprime el tamaño en bytes
print()


def crear_array2():
    array2 = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]]) #Creamos una array de 2x3
    return array2

my_array2 = crear_array2()
print("Array 2:\n", my_array2)
print("Número total de elementos:", my_array2.size)
print("Dimensión de la matriz:", my_array2.shape)
print("Tipo de elementos internos:", my_array2.dtype)
print("Tamaño de la matriz en bytes:", my_array2.nbytes)
print()

def crear_array3():
    array3 = np.array([[12], [4], [9], [8]]) #Creamos una array de 4x1
    return array3

my_array3 = crear_array3()
print("Array 3:\n", my_array3)
print("Número total de elementos:", my_array3.size)
print("Dimensión de la matriz:", my_array3.shape)
print("Tipo de elementos internos:", my_array3.dtype)
print("Tamaño de la matriz en bytes:", my_array3.nbytes)