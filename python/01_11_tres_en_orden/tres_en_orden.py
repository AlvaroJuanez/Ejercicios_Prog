'''
Programa: 01_11_tres_en_orden
El objetivo del programa es ordenar 3 numeros enteros, que seran introducidos por el usuario sin
importar el orden en el cual hayan sido introducido.

__author__ = "Alvaro Juanez M"
__version__ = "1.0" 27/02/2023
__status__ = "Aprendiendo python"
'''
# Incializa el programa indica al usuario los datos necesarios
print("Primer numero? ")
num_1 = int(input())
print("Segundo numero? ")
num_2 = int(input())
print("Tercer numero? ")
num_3 = int(input())

# Ordena los numero de menor a mayor
# Estas condiciones ordenan los numeros por la fuerza.
if num_1 < num_2 and num_2 < num_3:
    print(num_1, num_2, num_3)
elif num_1 < num_3 and num_3 < num_2:
    print(num_1, num_3, num_2)
elif num_2 < num_1 and num_3 > num_1:
    print(num_2, num_1, num_3)
elif num_3 < num_1 and num_1 < num_2:
    print(num_3, num_1, num_2)
elif num_3 < num_2 and num_2 < num_1:
    print(num_3, num_2, num_1)
elif num_2 < num_3 and num_3 < num_1:
    print(num_2, num_3, num_1)
